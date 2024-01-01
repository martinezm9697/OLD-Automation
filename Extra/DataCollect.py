import os
from time import sleep

from Bumble.BumbleScrapeTools import collect_images_for_training
from Edge import EdgeCommands


def collect_data():
    driver = EdgeCommands.nav_to_bumble()
    sleep(3)

    while len(os.path.dirname("Extra/images/dataset")) < 1000:
        collect_images_for_training(driver)
        from Bumble.BumbleAutomation import pass_bio
        pass_bio(driver)
        sleep(3)
