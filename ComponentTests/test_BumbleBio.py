from time import sleep
from unittest import TestCase

from Bumble.BumbleBio import BumbleBio
from Edge import EdgeCommands
from Bumble import BumbleScrapeTools as Bscrape
from time import sleep
from unittest import TestCase

from selenium.webdriver.common.by import By

import Edge.EdgeCommands as Edge
from config import TEST_BIO_PAGE, IMAGE_DIR

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
    def test_display_profile(self): 
        bumbleBio = BumbleBio(
            Bscrape.download_images_from_bio(self.driver, IMAGE_DIR + "\\"),
            Bscrape.get_bio_name(self.driver),
            Bscrape.get_bio_age(self.driver),
            Bscrape.get_photo_verified(self.driver),
            Bscrape.get_badges(self.driver),
            Bscrape.get_bio_height(self.driver),
            Bscrape.get_bio_occupation(self.driver),
            Bscrape.get_bio_school(self.driver),
            Bscrape.get_bio_exercise(self.driver),
            Bscrape.get_bio_education(self.driver),
            Bscrape.get_bio_drinking(self.driver),
            Bscrape.get_bio_smoking(self.driver),
            Bscrape.get_bio_gender(self.driver),
            Bscrape.get_bio_intentions(self.driver),
            Bscrape.get_bio_family_plans(self.driver),
            Bscrape.get_bio_star_sign(self.driver),
            Bscrape.get_bio_politics(self.driver),
            Bscrape.get_bio_religion(self.driver),
            Bscrape.get_bio_about_me(self.driver),
            Bscrape.get_bio_sections(self.driver),
            Bscrape.get_bio_locations(self.driver)
        )

        print(bumbleBio.display_profile())
    
