from time import sleep

from Bumble.BumbleBio import BumbleBio
from Bumble import BumbleScrapeTools as Scrape, BumbleRating
from Bumble.BumbleRating import sum_bio_ratings
from Edge import EdgeCommands
from config import IMAGE_DIR


def create_bio(driver):
    bumble_bio = BumbleBio(
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
    return bumble_bio


def like_bio(driver):
    EdgeCommands.click_bumble_like_button(driver)
    print("liked bio")


def pass_bio(driver):
    EdgeCommands.click_bumble_pass_button(driver)
    print("passed bio")


def rate_bio(bio):
    if BumbleRating.bio_has_dealbreaker(bio):
        return 0

    rating = sum_bio_ratings(bio)

    print(bio.name + " has a rating of " + str(rating))

    return rating


def rate_bios_until_end(driver):
    while True:
        bumble_bio = create_bio(driver)
        bumble_bio.display_profile()
        rating = rate_bio(bumble_bio)
        if rating > 7:
            print("Liking " + bumble_bio.name)
            like_bio(driver)
        else:
            print("Passing " + bumble_bio.name)
            pass_bio(driver)
        sleep(2)
