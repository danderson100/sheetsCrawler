Author: David Anderson

File: main.py

Purpose: This program is for WGU students. It uses Google Sheets API and Selenium Driver to
pull all LinkedIn addresses from the WGU LinkedIn Network Google sheet and controls a remote browser to
send requests to everyone on the list. This program may encounter problems if you are not at least a third connection
from the people in the list. Feel free to add me manually: https://www.linkedin.com/in/david-s-anderson/ 
Then you'll be 2nd connection with most people. The code should take about 10-15 minutes to add everyone (~165 invites), 
so you may need to ensure your monitor doesn't sleep.

SETUP INSTRUCTIONS:
------------------------------------------------------------------------------------------------------------------------
NOTE: I used an Ubuntu VM and PyCharm IDE while setting this up myself. However, most commands/info should work with MacOS, too. Windows you may have to do a little more digging on your own.

Step 1: Make a copy of the WGU LinkedIn Network Google Sheet: https://docs.google.com/spreadsheets/d/12HtPG9IdXnagrXGu9OGpSAOEcdc6GvG9vXjOT0aTbxU/edit?usp=sharing 

Click File -> Make a Copy. You can find the Google sheet by clicking above or going into the WGU-IT Slack channel and typing !linkedin. 
Store it in your own Google Drive and name it: Copy of WGU LinkedIn Network

Ensure you are logged into your Google account and have access to your Drive.

Step 2: You must first create your own client_secret.json file and enable the Google Drive AND Google Sheets APIs.
Follow these instructions:
    
    1.) Go to the Google APIs Console: https://console.developers.google.com/
    2.) Create a new project.
    3.) Click Enable API. Search for and enable the Google Drive API and the Google Sheets API.
    4.) Click Create credentials -> "Help me choose" -> Google Sheets API -> Web server -> Application data -> No, not using them.
    5.) Name the service account and grant it a Project Role of Editor.
    6.) Download the JSON file.
    7.) Copy the JSON file to your code directory and rename it to client_secret.json
    8.) Open your client_secret.json file. You will see an email address. 
    9.) SHARE the Copy of WGU LinkedIn Network sheet with that email address and give editor privileges.


NOTE: Make sure your client_secret.json file is in your working directory. If still stuck, more info can be found here: https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html

Step 3: Create your own Python project with a file named main.py. Install gspread: Open terminal, navigate to directory.

    pip install gspread
    
    NOTE: You may have to use this instead: pip3 install gspread

Step 4: Install Selenium for Python. If below doesn't work, more info can be found here: https://selenium-python.readthedocs.io/installation.html
 
    pip install -U selenium
    
    NOTE: You may have to use this instead: pip3 install -U selenium

Step 5: Get the Google Chrome chromedriver and install it.  Select the correct driver for your version
of chrome. If you are up-to-date it's likely either 88 or 89. Download page: https://chromedriver.chromium.org/downloads

Add it to your PATH (e.g. usr/local/bin/ or usr/bin/). Make sure you have Google Chrome installed. 

NOTE: You can type echo $PATH in terminal to show your path directories.

How to add chromedriver to PATH (Ubuntu/Linux) Should work with MacOS but you may have a different PATH:

    1.) Download it here if you haven't already: https://chromedriver.chromium.org/downloads

    2.) Extract the file with: tar -xvzf chromedriver*

    3.) Find the file named 'chromedriver' and make it executable: chmod +x chromedriver

    4.) Add the driver to your PATH: sudo mv chromedriver /usr/local/bin/



Step 6: Copy the main.py code into your own project. Go into the main.py code and enter your LinkedIn username and password where needed.
This will allow Selenium to login and add people to your network.

------------------------------------------------------------------------------------------------------------------------
USAGE INSTRUCTIONS:

Options:

A) Run from your IDE

B) Run from command line with ./main.py
