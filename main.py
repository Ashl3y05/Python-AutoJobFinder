from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions

import os
from time import time, sleep

USERNAME = os.environ["LINKEDIN_USER"]
PASSWORD = os.environ["LINKEDIN_PASS"]


def sign_in():
    enter = driver.find_element(By.LINK_TEXT, "Sign in")
    enter.click()

edge_option = webdriver.EdgeOptions()
edge_option.add_experimental_option("detach", True)

driver = webdriver.Edge(options=edge_option)
driver.get("https://www.linkedin.com/jobs/")

sign_in()

sleep(3)

user_text = driver.find_element(By.ID, "username")
pass_text = driver.find_element(By.ID, "password")

user_text.send_keys(USERNAME)
pass_text.send_keys(PASSWORD)

submit = driver.find_element(By.CSS_SELECTOR, ".login__form_action_container button")
submit.click()

sleep(3)

search_box = driver.find_element(By.CLASS_NAME, 'jobs-search-box__text-input--rounded')
search_box.send_keys("Python Developer", Keys.ENTER)

sleep(2)

jobs = driver.find_elements(By.CLASS_NAME, 'eXpUlPeraWOMWeQsOLgQAYzhjWpNMjOpAHpxA')
save_job = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div/div[6]/div/button')

for item in jobs:
    item.click()
    sleep(1)
    try:
        save_job.click()
    except selenium.common.StaleElementReferenceException:
        print("Error")


