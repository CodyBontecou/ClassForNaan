# Web scraping uses technology to grab data from the web
# The backbone of technologies like Google
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("http://www.google.com")
element = driver.find_element_by_class_name("gLFyf")
element.click()
element.send_keys("Hotspringers")
element.send_keys(Keys.RETURN)
element = driver.find_elements_by_class_name("g")[4]
element.click()

