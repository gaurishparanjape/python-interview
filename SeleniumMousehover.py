from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('http://www.spicejet.com')

ActionChains(driver).move_to_element(By.ID("ctl00_HyperLinkLogin"))

