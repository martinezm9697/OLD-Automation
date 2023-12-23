from time import sleep
from Edge import EdgeCommands
from Bumble import BumbleScrapeTools
from config import IMAGE_DIR

if __name__ == '__main__':
    print('OLD Automation Started')

    driver = EdgeCommands.nav_to_bumble()
    sleep(3)

    BumbleScrapeTools.download_images_from_bio(driver, IMAGE_DIR+"\\")
    BumbleScrapeTools.get_bio_name(driver)
    #var = BumbleScrapeTools.get_bio_aboutMe(driver)
    #var = BumbleScrapeTools.get_bio_sections(driver)

    #print(var)

    driver.close()

    print('OLD Automation Finished')


