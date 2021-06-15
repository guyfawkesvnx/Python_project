from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://fb.com")

email = driver.find_element_by_id("email")
email.send_keys("123")


password = driver.find_element_by_id("pass")
password.send_keys("123")

login = driver.find_element_by_name("login")
login.send_keys(Keys.ENTER)


# driver.quit()