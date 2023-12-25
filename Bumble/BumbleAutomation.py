from Bumble.BumbleBio import BumbleBio
from Bumble import BumbleScrapeTools as Scrape
from config import IMAGE_DIR


def create_bio(driver):
    bumbleBio = BumbleBio(
        Scrape.download_images_from_bio(driver, IMAGE_DIR + "\\"),
        Scrape.get_bio_name(driver),
        Scrape.get_bio_age(driver),
        Scrape.get_photo_verified(driver),
        Scrape.get_badges(driver),
        Scrape.get_bio_height(driver),
        Scrape.get_bio_occupation(driver),
        Scrape.get_bio_school(driver),
        Scrape.get_bio_exercise(driver),
        Scrape.get_bio_education(driver),
        Scrape.get_bio_drinking(driver),
        Scrape.get_bio_smoking(driver),
        Scrape.get_bio_gender(driver),
        Scrape.get_bio_intentions(driver),
        Scrape.get_bio_family_plans(driver),
        Scrape.get_bio_star_sign(driver),
        Scrape.get_bio_politics(driver),
        Scrape.get_bio_religion(driver),
        Scrape.get_bio_about_me(driver),
        Scrape.get_bio_sections(driver),
        Scrape.get_bio_locations(driver)
    )
    return bumbleBio

