import os
from time import sleep

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Edge, EdgeOptions
from Edge import EdgeCommands, EdgeConfig
from config import PARENT_BUMBLE_BIO_XPATH, BUMBLE_WEBSITE, BUMBLE_APP, MSEDGEDRIVER_EXE

url = BUMBLE_WEBSITE

options = EdgeOptions()
options.use_chromium = True

# To disable notifications
prefs = {"user_experience_metrics":
             {"personalization_data_consent_enabled": True}
         }
options.add_experimental_option("prefs", prefs)

# Add additional options as needed
options.add_argument("--disable-notifications")
options.add_argument("--disable-web-security")

# Instantiate the Edge driver with options
service = webdriver.ChromeService(executable_path=MSEDGEDRIVER_EXE)
driver = webdriver.Edge(service=service, options=options)

driver.get(url)
EdgeConfig.load_cookies(driver)
driver.get(BUMBLE_APP)