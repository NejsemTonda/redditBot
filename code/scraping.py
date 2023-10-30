import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os 
from bs4 import BeautifulSoup
import json 

'''
Scraping is going to be hard propably sinvce reddit's changes to is API. Might use manual scraping instead
'''

def get_html(urls):    
    driver = webdriver.Firefox()
    driver.get("https://www.reddit.com/login")
    
    username = "HappyLittleRedditBot"
    password = os.environ["reddit_password"]
    
    driver.find_element("id", "loginUsername").send_keys(username)
    driver.find_element("id", "loginPassword").send_keys(password)
    driver.find_element("xpath", "/html/body/div/main/div[1]/div/div[2]/form/fieldset[5]/button").click()
    time.sleep(8)

    response = []
    for target in urls:
        driver.get(target)
        response.append(driver.page_source)

    return response

