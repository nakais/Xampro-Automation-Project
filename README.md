# Xampro Automation Project

This project automates the user registration, login, and profile update workflows for the Xampro platform using Selenium WebDriver with Python.

## Project Files

- `user_data.json`: Stores user details for automated registration and login.
- `register_user.py`: Automates the user registration process.
- `login_user.py`: Automates the login process for the registered user.
- `update_profile.py`: Automates updating profile details such as Date of Birth, Gender, and Education for the logged-in user.

## Prerequisites

- Python 3.x
- Selenium WebDriver
- Google Chrome browser
- ChromeDriver (Ensure it matches the version of Chrome installed on your machine)

## Installation

1. Clone this repository to your local machine.
2. Install dependencies using pip:
   ```bash
   pip install selenium
   ```
3. Ensure ChromeDriver is installed and available in your PATH.

## Project Setup

1. Add user details in `user_data.json`:
   ```json
   [
       {
           "name": "Nazrul Islam",
           "email": "bupicehu@cyclelove.cc",
           "phone": "01621805259",
           "password": "password123"
       }
   ]  
  
2.Run the scripts in this order:
- `register_user.py` - for user registration
- `login_user.py` - for logging in with the registered user
- `update_profile.py` - for updating profile details

## Running the Scripts
To run each script, navigate to the project directory and use the following commands:

```bash
python register_user.py
python login_user.py
python update_profile.py
```

## Test Cases
https://docs.google.com/spreadsheets/d/1PJYRe2OAWdf-kIGRKrUCVLKmnn2R_n-VLvlvtyn46eg/edit?usp=sharing

## Known Issues (Bug Report)
https://docs.google.com/spreadsheets/d/1Ueelg219gH5O0AChaBBuaqlTooJhWT5_OTuqRJj6M0g/edit?usp=sharing

## Recorded Video
A complete project walkthrough can be found in the video recorded on Loom: https://www.loom.com/share/6098b991895f4e818a0832e7d8048f01?sid=bc3b88ef-8997-47ef-b430-914f7b6abd60

   
