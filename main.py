from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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

search_box = driver.find_element(By.XPATH, value='//*[@id="jobs-search-box-keyword-id-ember213"]')
search_box.send_keys("Python Developer", Keys.ENTER)


