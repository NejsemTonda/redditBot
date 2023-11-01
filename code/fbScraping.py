from selenium import webdriver
import os
import time
import re

driver = webdriver.Firefox()

fb = "https://www.facebook.com/messages/t/100008013121913"

driver.get(fb)

driver.find_element("xpath", "//*[text()='Allow all cookies']").click()
driver.find_element("id", "email").send_keys("happylittleredditbot01@gmail.com")
driver.find_element("id", "pass").send_keys(os.environ["reddit_password"])
driver.find_element("id", "loginbutton").click()
time.sleep(5)

data = driver.page_source
driver.quit()

pattern = r'>[^<]*reddit\.com/r/[^<]*<'
matches = re.findall(pattern, data)
matches = list(set(map(lambda x: x[1:-1], matches)))
print(matches)
