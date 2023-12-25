from Bumble.BumbleBio import BumbleBio
from Bumble import BumbleScrapeTools as Scrape, BumbleRating
from Edge import EdgeCommands
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


def like_bio(driver):
    EdgeCommands.click_bumble_like_button(driver)
    print("liked bio")


def pass_bio(driver):
    EdgeCommands.click_bumble_pass_button(driver)
    print("passed bio")


def rate_bio(bio):
    if BumbleRating.bio_has_dealbreaker(bio):
        return 0

    rating = \
        BumbleRating.rate_bio_name(bio) + \
        BumbleRating.rate_bio_age(bio) + \
        BumbleRating.rate_bio_photo_verified(bio) + \
        BumbleRating.rate_bio_occupation(bio) + \
        BumbleRating.rate_bio_school(bio) + \
        BumbleRating.rate_bio_height(bio) + \
        BumbleRating.rate_bio_exercise(bio) + \
        BumbleRating.rate_bio_education(bio) + \
        BumbleRating.rate_bio_drinking(bio) + \
        BumbleRating.rate_bio_smoking(bio) + \
        BumbleRating.rate_bio_gender(bio) + \
        BumbleRating.rate_bio_intentions(bio) + \
        BumbleRating.rate_bio_family_plans(bio) + \
        BumbleRating.rate_bio_star_sign(bio) + \
        BumbleRating.rate_bio_politics(bio) + \
        BumbleRating.rate_bio_religion(bio) + \
        BumbleRating.rate_bio_words(bio)

    print(bio.name + " has a rating of " + str(rating))

    return rating
