Author: David Anderson

File: main.py

Purpose: This program is for WGU students. It uses Google Sheets API and Selenium Driver to
pull all LinkedIn addresses from the WGU LinkedIn Network and controls a remote browser to
send requests to everyone on the list.

WARNING: The program may crash if you have a pending invitation for someone in the list.

SETUP INSTRUCTIONS:
------------------------------------------------------------------------------------------------------------------------
Step 1: Make a copy of the WGU LinkedIn Network Google Sheet by clicking File -> Make a Copy. Store it in your 
own Google Drive and name it: Copy of WGU LinkedIn Network

Ensure you are logged into your Google account and have access to your Drive.

Step 2: You must first create your own client_secret.json file and enable the Google Drive AND Google Sheets APIs.
Follow the instructions here: https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html
However, do NOT update this code. Follow along to create the Google API project, create your client_secret.json file,
install gspread, and share the new sheet with the email address located in your json file.

NOTE: Make sure your client_secret.json file is in your working directory.

Step 3: Install Selenium for Python. Get the Firefox geckodriver and install it. Add it to your PATH. Follow the
installation instructions here: https://pypi.org/project/selenium/  Make sure you have Firefox installed.

How to add geckodriver to PATH (Ubuntu/Linux):

    1.) Open terminal and download it with the following command: wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz

    2.) Extract the file with: tar -xvzf geckodriver*

    3.) Make it executable: chmod +x geckodriver

    4.) Add the driver to your PATH: sudo mv geckodriver /usr/local/bin/


Step 4: Go into the below code and enter your LinkedIn username and password where needed.
This will allow Selenium to login and add people to your network.

------------------------------------------------------------------------------------------------------------------------
USAGE INSTRUCTIONS:

Options:

A) Run from your IDE

B) Run from command line with ./main.py