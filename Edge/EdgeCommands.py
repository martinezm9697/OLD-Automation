import EdgeConfig


def nav_to_bumble():
    url = 'https://bumble.com'
    driver = EdgeConfig.configure_edge()
    driver.get(url)
    EdgeConfig.load_cookies(driver)
    driver.get(url + "/app")
    return driver