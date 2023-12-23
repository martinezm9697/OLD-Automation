import pickle

from selenium import webdriver
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver import DesiredCapabilities

from config import COOKIES_DIR, MSEDGEDRIVER_EXE


# Configure the Edge driver


def configure_edge():
    # Create options
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
    driver = webdriver.Edge(service=service)

    return driver


def attach_to_session(executor_url, session_id):
    original_execute = webdriver.remote.webdriver.WebDriver.execute

    def new_command_execute(self, command, params=None):
        if command == "newSession":
            # Mock the response to return the existing session_id
            return {'success': 0, 'value': None, 'sessionId': session_id}
        else:
            return original_execute(self, command, params)

    # Patch the function before creating the driver object
    webdriver.remote.webdriver.WebDriver.execute = new_command_execute

    driver = webdriver.Remote(command_executor=executor_url, desired_capabilities=DesiredCapabilities.EDGE)
    driver.session_id = session_id

    # Replace the patched function with original function
    webdriver.remote.webdriver.WebDriver.execute = original_execute

    return driver

    # Load Cookies


def load_cookies(driver):
    with open(COOKIES_DIR, "rb") as f:
        cookies = pickle.load(f)
    for cookie in cookies:
        driver.add_cookie(cookie)

