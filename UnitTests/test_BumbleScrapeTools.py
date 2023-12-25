import re
from time import sleep
from unittest import TestCase

from selenium.webdriver.common.by import By

import Edge.EdgeCommands as Edge
from Bumble import BumbleScrapeTools
from Config.Config import TEST_BIO_PAGE, IMAGE_DIR

class Test(TestCase):
    @classmethod
    def setUpClass(cls):
        print('Setting up the session')
        driver = Edge.nav_to_bumble()
        sleep(1)
        driver.get(TEST_BIO_PAGE)
        sleep(3)
        preview_button = driver.find_element(By.XPATH,
                                             '/html/body/div/div/div[1]/main/div/div[1]/div/section[1]/div/div[2]/div')
        preview_button.click()
        sleep(3)
        cls.driver = driver

    def test_download_images_from_src(self):
        BumbleScrapeTools.download_images_from_bio(self.driver, IMAGE_DIR)

        assert len(IMAGE_DIR + "\\") > 0

    def test_get_bio_name(self):
        name = BumbleScrapeTools.get_bio_name(self.driver)

        assert name

    def test_get_bio_age(self):
        age = BumbleScrapeTools.get_bio_age(self.driver)

        assert age

    def test_get_photo_verified(self):
        photo_verified = BumbleScrapeTools.get_photo_verified(self.driver)

        assert photo_verified

    def test_get_badges(self):
        badges = BumbleScrapeTools.get_badges(self.driver)

        assert badges

    def test_get_bio_height(self):
        height = BumbleScrapeTools.get_bio_height(self.driver)

        assert height

    def test_get_bio_occupation(self):
        occupation = BumbleScrapeTools.get_bio_occupation(self.driver)

        assert occupation

    def test_get_bio_school(self):
        schools = BumbleScrapeTools.get_bio_school(self.driver)

        assert schools

    def test_get_bio_exercise(self):
        exercise = BumbleScrapeTools.get_bio_exercise(self.driver)

        assert exercise

    def test_get_bio_education(self):
        education = BumbleScrapeTools.get_bio_education(self.driver)

        assert education

    def test_get_bio_smoking(self):
        smoking = BumbleScrapeTools.get_bio_smoking(self.driver)

        assert smoking

    def test_get_bio_drinking(self):
        drinking = BumbleScrapeTools.get_bio_drinking(self.driver)

        assert drinking

    def test_get_bio_gender(self):
        gender = BumbleScrapeTools.get_bio_drinking(self.driver)

        assert gender

    def test_get_bio_intentions(self):
        intentions = BumbleScrapeTools.get_bio_intentions(self.driver)

        assert intentions

    def test_get_bio_family_plans(self):
        family_plans = BumbleScrapeTools.get_bio_family_plans(self.driver)

        assert family_plans

    def test_get_bio_star_sign(self):
        star_sign = BumbleScrapeTools.get_bio_star_sign(self.driver)

        assert star_sign

    def test_get_bio_politics(self):
        politics = BumbleScrapeTools.get_bio_politics(self.driver)

        assert politics

    def test_get_bio_religion(self):
        religion = BumbleScrapeTools.get_bio_religion(self.driver)

        assert religion

    def test_get_bio_aboutMe(self):
        about_me = BumbleScrapeTools.get_bio_about_me(self.driver)

        assert about_me

    def test_get_bio_sections(self):
        sections = BumbleScrapeTools.get_bio_sections(self.driver)

        assert sections

    def test_get_bio_current_location(self):
        current_location = BumbleScrapeTools.get_bio_current_location(self.driver)

        assert current_location

    def test_get_bio_lives_in_location(self):
        lives_in_location = BumbleScrapeTools.get_bio_lives_in_location(self.driver)

        assert lives_in_location

    def test_get_bio_city(self):
        city = BumbleScrapeTools.get_bio_city(self.driver)

        assert re.match(r'^[a-zA-Z0-9_]+$', city)

    def test_get_bio_state(self):
        state = BumbleScrapeTools.get_bio_state(self.driver)

        assert re.match(r'^[a-zA-Z0-9_]+$', state)

    def test_get_bio_from_location(self):
        from_location = BumbleScrapeTools.get_bio_from_location(self.driver)

        assert re.match(r'^[a-zA-Z0-9_]+$', from_location)
