from selenium import webdriver
from selenium.webdriver.common.by import By

USERNAME = ""
PASSWORD = ""
edge_option = webdriver.EdgeOptions()
edge_option.add_experimental_option("detach", True)

driver = webdriver.Edge(options=edge_option)
driver.get("https://www.linkedin.com/jobs/")

sign_in = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in.click()