import pickle
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("--user-data-dir=chrome-data")

browser = webdriver.Chrome(executable_path = "./chromedriver", options=chrome_options)
browser.get('https://www.facebook.com')
#chrome_options.add_argument("user-data-dir=chrome-data")

fb_username = "EMAIL/PHONE"
fb_password = "PASSWORD"

username = browser.find_element_by_id("email")
password = browser.find_element_by_id("pass")
submit   = browser.find_element_by_id("u_0_b")
username.send_keys(fb_username)
password.send_keys(fb_password)

submit.click()

wait = WebDriverWait( browser, 5)
