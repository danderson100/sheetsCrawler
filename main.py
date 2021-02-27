"""
Author: David Anderson
File: main.py

Purpose: This program is for WGU students. It uses Google Sheets API and an PyAutoGUI to
pull all LinkedIn addresses from the WGU LinkedIn Network and controls mouse movements to
send requests to everyone on the list.

SETUP INSTRUCTIONS:
Step 1: Make a copy of the WGU LinkedIn Network Google Sheet and name it: Copy of WGU LinkedIn Network

Step 2: You must first create your own client_secret.json file and enable the Google Drive and Google Sheets APIs.
Follow the instructions here: https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html
However, do NOT update the code. Follow along to create the Google API project, create your client_secret.json file,
install gspread, and share the new sheet with the generated email located in your json file.

Step 3: Install PyAutoGUI. Follow these instructions according to your operating system:
https://pyautogui.readthedocs.io/en/latest/install.html#linux

Step 4:

"""
import gspread
import webbrowser
import pyautogui

scope = ['https://www.googlapis.com/feeds',
         'https://www.googlapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive.file',
         'https://www.googlapis.com/auth/drive']

pyautogui.FAILSAFE = True  # if you move the mouse to upper-left corner of screen it aborts


def get_urls():
    # Use a breakpoint in the code line below to debug your script.

    gc = gspread.service_account(filename="client_secret.json")

    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    sheet = gc.open("Copy of WGU LinkedIn Network").sheet1

    # Extract and store all linkedin URLS
    values_list = sheet.col_values(2)

    return values_list


def open_browser_tabs(urls):
    for url in urls:
        if url.startswith('https'):
            webbrowser.open_new_tab(url)
            add_user()
            break


def add_user():
    pyautogui.PAUSE = 2.5


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    list_of_urls = get_urls()
    open_browser_tabs(list_of_urls)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
