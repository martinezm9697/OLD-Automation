from time import sleep
from unittest import TestCase

from selenium.webdriver.common.by import By

from config import BUMBLE_APP

import Edge.EdgeCommands as Edge


class Test(TestCase):
    @classmethod
    def setUpClass(cls):
        print('Setting up the session')
        driver = Edge.nav_to_bumble()
        sleep(3)
        cls.driver = driver

    def test_click_bumble_pass_button(self):
        button = Edge.click_bumble_pass_button(self.driver)
        assert button

    def test_click_bumble_like_button(self):
        button = Edge.click_bumble_like_button(self.driver)
        assert button

    def test_click_bumble_superlike_button(self):
        button = Edge.click_bumble_superlike_button(self.driver)
        assert button
