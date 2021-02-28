Author: David Anderson

File: main.py

Purpose: This program is for WGU students. It uses Google Sheets API and Selenium Driver to
pull all LinkedIn addresses from the WGU LinkedIn Network Google sheet and controls a remote browser to
send requests to everyone on the list.

SETUP INSTRUCTIONS:
------------------------------------------------------------------------------------------------------------------------
Step 1: Make a copy of the WGU LinkedIn Network Google Sheet by clicking File -> Make a Copy. Store it in your 
own Google Drive and name it: Copy of WGU LinkedIn Network

Ensure you are logged into your Google account and have access to your Drive.

Step 2: You must first create your own client_secret.json file and enable the Google Drive AND Google Sheets APIs.
Follow these instructions:
    
    1.) Go to the Google APIs Console: https://console.developers.google.com/
    2.) Create a new project.
    3.) Click Enable API. Search for and enable the Google Drive API.
    4.) Create credentials for a Web Server to access Application Data.
    5.) Name the service account and grant it a Project Role of Editor.
    6.) Download the JSON file.
    7.) Copy the JSON file to your code directory and rename it to client_secret.json


NOTE: Make sure your client_secret.json file is in your working directory.

Step 3: Install gspread: Open terminal, navigate to directory.

    pip3 install gspread

Step 4: Install Selenium for Python.
 
    pip3 install -U selenium

Step 5: Get the Firefox geckodriver and install it. Add it to your PATH. You can also follow the installation instructions here: https://pypi.org/project/selenium/  Make sure you have Firefox installed. 

How to add geckodriver to PATH (Ubuntu/Linux):

    1.) Open terminal and download it with the following command: wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz

    2.) Extract the file with: tar -xvzf geckodriver*

    3.) Make it executable: chmod +x geckodriver

    4.) Add the driver to your PATH: sudo mv geckodriver /usr/local/bin/


Step 6: Go into the main.py code and enter your LinkedIn username and password where needed.
This will allow Selenium to login and add people to your network.

------------------------------------------------------------------------------------------------------------------------
USAGE INSTRUCTIONS:

Options:

A) Run from your IDE

B) Run from command line with ./main.py