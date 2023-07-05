from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import helpers
import string
import time
import constants

service = Service(executable_path=constants.EXECUTABLE_PATH)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get(constants.URL)

def check_form():
    form = driver.find_element(By.ID, "automationtestform")
    inputs = form.find_elements(By.TAG_NAME, "input")
    for inp in inputs:
        pass

def check_iframe_without_id():
    pass

def check_iframe_with_id():
    pass

if __name__ == "__main__":
    check_form()