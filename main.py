from time import sleep

from Bumble.BumbleBio import BumbleBio
from Edge import EdgeCommands
from Bumble import BumbleScrapeTools as Bscrape, BumbleAutomation
from config import IMAGE_DIR

if __name__ == '__main__':
    print('OLD Automation Started')

    driver = EdgeCommands.nav_to_bumble()
    sleep(3)

    bumbleBio = BumbleAutomation.create_bio(driver)
    print(bumbleBio.display_profile())


    driver.close()

    print('OLD Automation Finished')


