# Print a tide calendar for a location

A python program to retrieve tide data for a station, year, and month then create a calendar page (or pages) using `pcal`.

## Quick start

Install `pcal` (example uses brew on MacOS):

```bash
brew install pcal
```

Run this:

```bash
python3 -m venv tide-env
source tide-env/bin/activate
pip install requests
```

Then this, replacing the tide station, year, and month with your choices:

```bash
python3 get_tide_data.py --station_id 9449639 --year 2024 --month 6
```

You'll see a new PDF file created in the same directory with the tide calendar.

After you're finished making calendars, run this to clean up:

```bash
deactivate
```

If you want tide calendars for June through December 2024, run this complete script:

```bash
python3 -m venv tide-env
source tide-env/bin/activate
pip install requests
python3 get_tide_data.py --station_id 9449639 --year 2024 --month 6
python3 get_tide_data.py --station_id 9449639 --year 2024 --month 7
python3 get_tide_data.py --station_id 9449639 --year 2024 --month 8
python3 get_tide_data.py --station_id 9449639 --year 2024 --month 9
python3 get_tide_data.py --station_id 9449639 --year 2024 --month 10
python3 get_tide_data.py --station_id 9449639 --year 2024 --month 11
python3 get_tide_data.py --station_id 9449639 --year 2024 --month 12
deactivate
```

## Virtual environment

`python3 -m venv tide-env`

`source tide-env/bin/activate`

`pip install requests`

## Carlotta

Setting up and running Python scripts in a virtual environment is a great way to manage dependencies and ensure that your projects don't interfere with each other. Here's a step-by-step guide on how to do it:

### Step 1: Install Python

First, ensure you have Python installed. Most systems come with Python pre-installed. You can check by running `python --version` or `python3 --version` in your terminal or command prompt. If you don't have Python, download it from [python.org](https://www.python.org/).

### Step 2: Create a Virtual Environment

Navigate to the directory where you want your project to reside using the terminal or command prompt. Then, run the following command to create a virtual environment. Replace `myenv` with the name you want to give to your virtual environment.

For **Unix/macOS**:

```bash
python3 -m venv myenv
```

For **Windows**:

```cmd
python -m venv myenv
```

This command creates a folder named `myenv` (or whatever you named it) in your current directory, which contains the Python interpreter, the standard library, and various supporting files.

### Step 3: Activate the Virtual Environment

Before you install packages or run your script, you need to activate the virtual environment.

For **Unix/macOS**:

```bash
source myenv/bin/activate
```

For **Windows** (Command Prompt):

```cmd
myenv\Scripts\activate.bat
```

For **Windows** (PowerShell):

```powershell
myenv\Scripts\Activate.ps1
```

You'll know the virtual environment is activated because its name will appear at the beginning of the terminal prompt, indicating that the Python interpreter in the virtual environment will be used.

### Step 4: Install Dependencies

With the virtual environment activated, install any dependencies your script requires. For your script, you need `requests`. Install it using `pip`:

```bash
pip install requests
```

### Step 5: Run Your Script

Now, navigate to the directory where your script is located (if you're not already there) and run it using Python. Assuming your script is named `script_name.py`:

```bash
python get_tide_data.py
```

And if you're using command line arguments:

```bash
python3 get_tide_data.py --station_id 9449639 --year 2024 --month 6
```

### Step 6: Deactivate the Virtual Environment

Once you're done working in the virtual environment, you can deactivate it by running:

```bash
deactivate
```

This returns you to the system's default Python interpreter.

### Tips

- **Organizing Projects**: Keep each of your Python projects in separate directories with their own virtual environments to manage dependencies effectively.
- **Requirements File**: If your project depends on multiple packages, consider creating a `requirements.txt` file listing all your dependencies. You can then install all of them at once using `pip install -r requirements.txt`.
