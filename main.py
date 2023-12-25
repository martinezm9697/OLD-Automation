from time import sleep

from Bumble.BumbleAutomation import rate_bios_until_end
from Bumble.BumbleBio import BumbleBio
from Edge import EdgeCommands
from Bumble import BumbleScrapeTools as Bscrape, BumbleAutomation, BumbleRating as Brate
from config import IMAGE_DIR

if __name__ == '__main__':
    print('OLD Automation Started')

    driver = EdgeCommands.nav_to_bumble()
    sleep(3)

    # bumbleBio = BumbleAutomation.create_bio(driver)
    # print(bumbleBio.display_profile())
    #
    # bio_rating = BumbleAutomation.rate_bio(bumbleBio)
    #
    # if bio_rating >= 5:
    #     print("Liking " + bumbleBio.name)
    #     BumbleAutomation.like_bio(driver)
    # else:
    #     print("Passing " + bumbleBio.name)
    #     BumbleAutomation.pass_bio(driver)
    rate_bios_until_end(driver)

    driver.close()

    print('OLD Automation Finished')


