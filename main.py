"""
Author: David Anderson
File: main.py

Purpose: This program is for WGU students. It uses Google Sheets API and Selenium Driver to
pull all LinkedIn addresses from the WGU LinkedIn Network and controls a remote browser to
send requests to everyone on the list.

SETUP INSTRUCTIONS:
------------------------------------------------------------------------------------------------------------------------
Step 1: Make a copy of the WGU LinkedIn Network Google Sheet and name it: Copy of WGU LinkedIn Network. Ensure you are
logged into your Google account and have access to your Drive.

Step 2: You must first create your own client_secret.json file and enable the Google Drive AND Google Sheets APIs.
Follow the instructions here: https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html
However, do NOT update this code. Follow along to create the Google API project, create your client_secret.json file,
install gspread, and share the new sheet with the email address located in your json file.

NOTE: Make sure your client_secret.json file is in your working directory.

Step 3: Install Selenium for Python. Get the Firefox geckodriver and install it. Add it to your PATH. Follow the
installation instructions here: https://pypi.org/project/selenium/  Make sure you have Firefox installed.

How to add geckodriver to PATH (Ubuntu/Linux):
    1.) Open terminal and download it with the following command:
wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz

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

"""
import gspread
import time
from selenium import webdriver

scope = ['https://www.googlapis.com/feeds',
         'https://www.googlapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive.file',
         'https://www.googlapis.com/auth/drive']


def get_urls():
    # Your client_secret.json file must be in working directory
    gc = gspread.service_account(filename="client_secret.json")

    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    sheet = gc.open("Copy of WGU LinkedIn Network").sheet1

    # Extract and store all linkedin URLS
    values_list = sheet.col_values(2)

    return values_list


def open_browser(urls):
    browser = webdriver.Firefox()
    browser.get('https://www.linkedin.com/')
    username = browser.find_element_by_id("session_key")
    password = browser.find_element_by_id("session_password")

    username.send_keys("your_username_here")  # Your LinkedIn username goes here
    password.send_keys("your_password_here")  # Your LinkedIn password goes here

    browser.find_element_by_class_name("sign-in-form__submit-button").click()

    for url in urls:
        if url.startswith('https'):
            browser.get(url)
            browser.find_element_by_class_name("pv-s-profile-actions--connect").click()
            browser.find_element_by_class_name("ml1").click()
            time.sleep(2.5)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    list_of_urls = get_urls()
    open_browser(list_of_urls)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
