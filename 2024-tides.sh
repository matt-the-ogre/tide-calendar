#!/bin/bash

# print all months for 2024

# note: pcal and ps2pdf must be installed before running

python3 -m venv tide-env
source tide-env/bin/activate
pip install requests
python3 get_tide_data.py --station_id 9449639 --year 2024 --month 1
python3 get_tide_data.py --station_id 9449639 --year 2024 --month 2
python3 get_tide_data.py --station_id 9449639 --year 2024 --month 3
python3 get_tide_data.py --station_id 9449639 --year 2024 --month 4
python3 get_tide_data.py --station_id 9449639 --year 2024 --month 5
python3 get_tide_data.py --station_id 9449639 --year 2024 --month 6
python3 get_tide_data.py --station_id 9449639 --year 2024 --month 7
python3 get_tide_data.py --station_id 9449639 --year 2024 --month 8
python3 get_tide_data.py --station_id 9449639 --year 2024 --month 9
python3 get_tide_data.py --station_id 9449639 --year 2024 --month 10
python3 get_tide_data.py --station_id 9449639 --year 2024 --month 11
python3 get_tide_data.py --station_id 9449639 --year 2024 --month 12
deactivate
