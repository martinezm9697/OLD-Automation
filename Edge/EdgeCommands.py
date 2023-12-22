import Edge.EdgeConfig as EdgeConfig
from config import BUMBLE_WEBSITE, BUMBLE_APP


def nav_to_bumble():
    url = BUMBLE_WEBSITE
    driver = EdgeConfig.configure_edge()
    driver.get(url)
    EdgeConfig.load_cookies(driver)
    driver.get(BUMBLE_APP)
    return driver
