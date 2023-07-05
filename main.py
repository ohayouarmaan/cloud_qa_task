from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support.ui import Select
import helpers
import os
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
    password = helpers.random_string(10)
    for inp in inputs:
        inp_type = inp.get_attribute("type")
        if inp_type == "text":
            if inp.get_attribute("id") == "dob":
                inp.send_keys(helpers.random_date())
            else:
                inp.send_keys(helpers.random_string(10))
        elif inp_type == "email":
            inp.send_keys(helpers.random_email(10))
        elif inp_type in ["radio", "checkbox"]:
            inp.click()
        elif inp_type == "password":
            inp.send_keys(password)
        elif inp_type == "number":
            inp.send_keys(helpers.random_number(10))
        elif inp_type == "file":
            inp.send_keys(os.path.abspath("./test_file.txt"))


    text_areas = form.find_elements(By.TAG_NAME, "textarea")
    for text_area in text_areas:
        try:
            text_area.send_keys(helpers.random_string(50))
        except Exception as _:
            iframe = WebDriverWait(driver, 10).until(lambda x: x.find_element(By.ID, "mytextarea_ifr"))
            driver.switch_to.frame(iframe)
            p = driver.find_element(By.TAG_NAME, "p")
            p.send_keys(helpers.random_string(40))
            driver.switch_to.default_content()


    select = Select(form.find_element(By.TAG_NAME, "select"))
    print(select)
    select.select_by_index(1)
    time.sleep(1)
    for inp in form.find_elements(By.TAG_NAME, "button"):
        if inp.get_attribute("type") == "submit":
            inp.click()
            break
    time.sleep(10)

def check_iframe_without_id():
    pass

def check_iframe_with_id():
    pass

if __name__ == "__main__":
    check_form()