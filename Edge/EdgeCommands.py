from telnetlib import EC
from time import sleep

from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import Edge.EdgeConfig as EdgeConfig
from config import BUMBLE_WEBSITE, BUMBLE_APP, BUMBLE_LIKE_BUTTON_CLASS, BUMBLE_PASS_BUTTON_CLASS, \
    BUMBLE_SUPERLIKE_BUTTON_CLASS


def nav_to_bumble():
    url = BUMBLE_WEBSITE
    driver = EdgeConfig.configure_edge()
    driver.get(url)
    EdgeConfig.load_cookies(driver)
    driver.get(BUMBLE_APP)
    return driver


def get_page_html(driver, page):
    driver.get(page)
    return driver.page_source


def click_bumble_like_button(driver):
    like_button = driver.find_element(By.CSS_SELECTOR, "div[class='{}']".format(BUMBLE_LIKE_BUTTON_CLASS))
    like_button.click()
    return like_button


def click_bumble_pass_button(driver):
    pass_button = driver.find_element(By.CSS_SELECTOR, "div[class='{}']".format(BUMBLE_PASS_BUTTON_CLASS))
    pass_button.click()
    return pass_button


def click_bumble_superlike_button(driver):
    superlike_button = driver.find_element(By.CSS_SELECTOR, "div[class='{}']".format(BUMBLE_SUPERLIKE_BUTTON_CLASS))
    superlike_button.click()
    return superlike_button
