import gspread
import time
from selenium import webdriver

scope = ['https://www.googlapis.com/feeds',
         'https://www.googlapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive.file',
         'https://www.googlapis.com/auth/drive']


# Purpose: This function uses gspread and the credentials you created in json format
# to access the WGU LinkedIn Network Google sheet. It then retrieves all
# URLs from that document and stores them.
#
# @:return values_list is the list of urls scraped from "Copy of WGU LinkedIn Network"
def get_urls():
    # Your client_secret.json file must be in working directory
    gc = gspread.service_account(filename="client_secret.json")

    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    sheet = gc.open("Copy of WGU LinkedIn Network").sheet1

    # Extract and store all linkedin URLS
    values_list = sheet.col_values(2)

    return values_list


# Purpose: This function creates a Selenium-controlled instance of Chrome, logs
# in using the provided credentials, goes through all of the urls from
# the WGU Google sheet, and clicks the send request button. The thread sleeps
# for 2.5 seconds between each
#
# @:parameter urls is the list of urls scraped from "Copy of WGU LinkedIn Network"
def open_browser(urls):
    browser = webdriver.Chrome()
    browser.get('https://www.linkedin.com/')
    username = browser.find_element_by_id("session_key")
    password = browser.find_element_by_id("session_password")

    username.send_keys("your_username_here")  # Your LinkedIn username goes here
    password.send_keys("your_password_here")  # Your LinkedIn password goes here

    browser.find_element_by_class_name("sign-in-form__submit-button").click()

    for url in urls:
        if url.startswith('https'):
            browser.get(url)
            distance = browser.find_element_by_class_name("dist-value")

            if distance.text == "1st":
                continue  # We have already added that person, so skip this iteration
            elif distance.text == "2nd":
                browser.find_element_by_class_name("pv-s-profile-actions--connect").click()
            else:
                # do third or no connection stuff
                browser.find_element_by_class_name("pv-s-profile-actions__overflow-toggle").click()
                time.sleep(1)
                browser.find_element_by_class_name("pv-s-profile-actions--connect").click()

            browser.find_element_by_class_name("ml1").click()
            time.sleep(2.5)

    browser.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    list_of_urls = get_urls()
    open_browser(list_of_urls)
