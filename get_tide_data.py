import argparse
import requests
from datetime import datetime
import calendar
import subprocess
import logging

# sample call: python get_tide_data.py --station_id 9449639 --year 2024 --month 6

def convert_tide_data_to_pcal(tide_data_filename, pcal_filename):
    """
    Converts tide data to a pcal compatible custom dates file.

    Parameters:
    - tide_data_filename: The path to the file containing the tide data.
    - pcal_filename: The path to the output pcal custom dates file.
    """
    # Open the tide data file and the output pcal file
    with open(tide_data_filename, 'r') as tide_file, open(pcal_filename, 'w') as pcal_file:
        # Skip the header line
        next(tide_file)
        
        for line in tide_file:
            # Parse the tide data
            date_time, prediction, tide_type = line.strip().split(',')

            # round prediction to one decimal place
            prediction = round(float(prediction), 1)

            date, time = date_time.split()
            year, month, day = date.split('-')
            
            # Convert tide type from single character to full word
            tide_type_full = "High" if tide_type == "H" else "Low"
            
            # Format the date for pcal (mm/dd)
            pcal_date = f"{int(month)}/{int(day)}"
            
            if prediction < 1.0:
                # add an asterisk to the pcal_date if the tide is less than 1.0 meter
                # this indicates the day is special to pcal and it will be colour-coded
                pcal_date += "*"
            
            # Write the event to the pcal file
            # Including time and tide type in the event description
            pcal_file.write(f"{pcal_date}  {time} {tide_type_full} {prediction} m\n")


def download_tide_data(station_id, year, month):
    # Calculate the last day of the month
    _, last_day = calendar.monthrange(year, month)

    # Construct the request URL based on the provided sample API call
    base_url = "https://api.tidesandcurrents.noaa.gov/api/prod/datagetter"
    params = {
        "begin_date": f"{year}{month:02d}01",
        "end_date": f"{year}{month:02d}{last_day}",
        "station": station_id,
        "product": "predictions",
        "datum": "MLLW",
        "time_zone": "lst_ldt",
        "interval": "hilo",
        "units": "metric",
        "format": "csv",
    }

    # Make the request
    response = requests.get(base_url, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Save the response content to a CSV file
        filename = f"{station_id}_{year}_{month:02d}.csv"
        with open(filename, 'wb') as file:
            file.write(response.content)
        logging.debug(f"Data successfully saved to {filename}")
    else:
        logging.error(f"Failed to download data: {response.status_code}")

if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser(description="Download tide data as CSV.")
    parser.add_argument('--station_id', type=str, default='9449639', help='Station ID (default: 9449639)')
    parser.add_argument('--year', type=int, default=datetime.now().year, help='Year (default: current year)')
    parser.add_argument('--month', type=int, default=datetime.now().month, help='Month (default: current month)')
    
    args = parser.parse_args()

    # Ensure month is in the correct format
    if args.month < 1 or args.month > 12:
        logging.error("Month must be between 1 and 12")
    else:
        download_tide_data(args.station_id, args.year, args.month)

    # convert the tide data to pcal format
    downloaded_filename = f"{args.station_id}_{args.year}_{args.month:02d}.csv"
    # make a pcal file with the tide events using the month and year in the filename
    pcal_filename = f"pcal_tide_events_{args.year}_{args.month:02d}.txt"
    
    convert_tide_data_to_pcal(downloaded_filename, pcal_filename)

    logging.debug(f"PCAL file created: {pcal_filename}")

    # now make a calendar page using `pcal` and the pcal file with the tide events for that month and year
    # print("To create a calendar page with the tide events, run the following command:")
    # print(f"pcal -f {pcal_filename} -o {pcal_filename.replace('.txt', '.ps')}")
    # print("This will create a PostScript file that you can print or view.")
    # print("You can also convert the PostScript file to PDF using `ps2pdf`.")
    # print("For example: `ps2pdf pcal_tide_events_2024_06.ps pcal_tide_events_2024_06.pdf`")
    # print("This will create a PDF file that you can view or print.")
    # print("You can also customize the appearance of the calendar page using pcal options.")
    # print("For more information, see the pcal documentation.")
    # print("https://manpages.debian.org/testing/pcal/pcal.1.en.html")

    # Call the shell command to create the calendar page
    subprocess.run(["pcal", "-f", pcal_filename, "-o", pcal_filename.replace('.txt', '.ps'), "-s 1.0:0.0:0.0", "-m", "-S", str(args.month), str(args.year)])

    # Convert the PostScript file to PDF
    subprocess.run(["ps2pdf", pcal_filename.replace('.txt', '.ps'), pcal_filename.replace('.txt', '.pdf')])

    # delete the PostScript file
    subprocess.run(["rm", pcal_filename.replace('.txt', '.ps')])
    # delete the CSV file
    subprocess.run(["rm", downloaded_filename])
    # delete the pcal file
    subprocess.run(["rm", pcal_filename])

    # Print a message indicating the PDF file creation
    logging.info(f"PDF file created: {pcal_filename.replace('.txt', '.pdf')}")
    # call the shell command to create the calendar page
