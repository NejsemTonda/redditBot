#import praw
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os 
'''
Scraping is going to be hard propably sinvce reddit's changes to is API. Might use manual scraping instead
'''


driver = webdriver.Firefox()
driver.get("https://www.reddit.com/")

username = "HappyLittleRedditBot"
password = os.environ["reddit_password"]

login_button = driver.find_element("link text", "Log In")
login_button.click()


