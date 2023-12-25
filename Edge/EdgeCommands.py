from selenium.webdriver.common.by import By

import Edge.EdgeConfig as EdgeConfig
from config import BUMBLE_WEBSITE, BUMBLE_APP, BUMBLE_LIKE_BUTTON_XPATH, BUMBLE_PASS_BUTTON_XPATH, \
    BUMBLE_SUPERLIKE_BUTTON_XPATH


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
    like_button = driver.find_element(By.XPATH, BUMBLE_LIKE_BUTTON_XPATH)
    like_button.click()
    return driver


def click_bumble_pass_button(driver):
    pass_button = driver.find_element(By.XPATH, BUMBLE_PASS_BUTTON_XPATH)
    pass_button.click()
    return driver


def click_bumble_superlike_button(driver):
    superlike_button = driver.find_element(By.XPATH, BUMBLE_SUPERLIKE_BUTTON_XPATH)
    superlike_button.click()
    return driver
