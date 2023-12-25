import os
import requests
import re

from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

from config import PARENT_BUMBLE_CLASS_NAME


def get_list_of_src_from_element(element):
    html = element.get_attribute('innerHTML')

    soup = BeautifulSoup(html, 'html.parser')

    elem_list = soup.find_all('img', 'media-box__picture-image')

    for i in range(len(elem_list)):
        elem_list[i] = elem_list[i]['src']

    return (elem_list)


def download_images_from_src(src_list, destination):
    images = []
    for i, src in enumerate(src_list):
        image_url = 'http:' + src
        images.append(image_url)

        if not os.path.exists(destination):
            os.makedirs(destination)

        r = requests.get(image_url, stream=True)
        if r.status_code == 200:

            with open(os.path.join(destination, 'image{}.jpg'.format(i)), 'wb') as f:
                f.write(r.content)
    return images


def download_images_from_bio(driver, des):
    parent_elem = driver.find_element(By.CLASS_NAME, PARENT_BUMBLE_CLASS_NAME)
    src_list = get_list_of_src_from_element(parent_elem)
    images = download_images_from_src(src_list, des)
    return images

def get_bio_name(driver):
    name = driver.find_element(By.CLASS_NAME, 'encounters-story-profile__name')
    return name.text


def get_bio_age(driver):
    try:
        age = driver.find_element(By.CLASS_NAME, 'encounters-story-profile__age')
        age = re.split(r',', age.text)[1].strip(" ")
        return age
    except:
        return ""


def get_photo_verified(driver):
    try:
        photo_verified = driver.find_element(By.CLASS_NAME, 'encounters-story-profile__verification-badge')
        if photo_verified:
            return True
    except:
        return False



def get_badges(driver):
    try:
        parent_elem = driver.find_element(By.CLASS_NAME, PARENT_BUMBLE_CLASS_NAME)

        html = parent_elem.get_attribute('innerHTML')
        soup = BeautifulSoup(html, 'html.parser')

        badges_child_elements = (soup.find('ul', 'encounters-story-about__badges')
                                 .find_all('li', 'encounters-story-about__badge'))

        badges = []
        for badge in badges_child_elements:
            badges.append(badge.text)
        return badges
    except:
        return []


def get_bio_height(driver):
    try:
        parent_elem = driver.find_element(By.CLASS_NAME, PARENT_BUMBLE_CLASS_NAME)

        html = parent_elem.get_attribute('innerHTML')

        soup = BeautifulSoup(html, 'html.parser')

        height = soup.find('img',
                           src=re.compile(".*_height.*"))

        return height['alt']
    except:
        return ""


def get_bio_occupation(driver):
    try:
        parent_elem = driver.find_element(By.CLASS_NAME, PARENT_BUMBLE_CLASS_NAME)
        html = parent_elem.get_attribute('innerHTML')
        soup = BeautifulSoup(html, 'html.parser')
        occupation = soup.find('p', 'encounters-story-profile__occupation')
        return occupation.text
    except:
        return ""


def get_bio_school(driver):
    try:
        parent_elem = driver.find_element(By.CLASS_NAME, PARENT_BUMBLE_CLASS_NAME)
        html = parent_elem.get_attribute('innerHTML')
        soup = BeautifulSoup(html, 'html.parser')
        school = soup.find('p', 'encounters-story-profile__education')
        return school.text
    except:
        return ""


def get_bio_exercise(driver):
    try:
        parent_elem = driver.find_element(By.CLASS_NAME, PARENT_BUMBLE_CLASS_NAME)

        html = parent_elem.get_attribute('innerHTML')

        soup = BeautifulSoup(html, 'html.parser')

        exercise = soup.find('img',
                             src=re.compile(".*_exercise.*"))
        return exercise['alt']
    except:
        return ""


def get_bio_education(driver):
    try:
        parent_elem = driver.find_element(By.CLASS_NAME, PARENT_BUMBLE_CLASS_NAME)

        html = parent_elem.get_attribute('innerHTML')

        soup = BeautifulSoup(html, 'html.parser')

        education = soup.find('img',
                              src=re.compile(".*_education.*"))
        return education['alt']
    except:
        return ""


def get_bio_drinking(driver):
    try:
        parent_elem = driver.find_element(By.CLASS_NAME, PARENT_BUMBLE_CLASS_NAME)

        html = parent_elem.get_attribute('innerHTML')

        soup = BeautifulSoup(html, 'html.parser')

        drinking = soup.find('img',
                             src=re.compile(".*_drinking.*"))
        return drinking['alt']
    except:
        return ""


def get_bio_smoking(driver):
    try:
        parent_elem = driver.find_element(By.CLASS_NAME, PARENT_BUMBLE_CLASS_NAME)

        html = parent_elem.get_attribute('innerHTML')

        soup = BeautifulSoup(html, 'html.parser')

        smoking = soup.find('img',
                            src=re.compile(".*_smoking.*"))
        return smoking['alt']
    except:
        return ""


def get_bio_gender(driver):
    try:
        parent_elem = driver.find_element(By.CLASS_NAME, PARENT_BUMBLE_CLASS_NAME)

        html = parent_elem.get_attribute('innerHTML')

        soup = BeautifulSoup(html, 'html.parser')

        politics = soup.find('img',
                             src=re.compile(".*_gender.*"))
        return politics['alt']
    except:
        return ""


def get_bio_intentions(driver):
        try:
            parent_elem = driver.find_element(By.CLASS_NAME, PARENT_BUMBLE_CLASS_NAME)
            html = parent_elem.get_attribute('innerHTML')
            soup = BeautifulSoup(html, 'html.parser')
            dating_intentions = soup.find('img',
                                          src=re.compile(".*_intentions.*"))
            return dating_intentions['alt']
        except:
            return ""


def get_bio_family_plans(driver):
    try:
        parent_elem = driver.find_element(By.CLASS_NAME, PARENT_BUMBLE_CLASS_NAME)

        html = parent_elem.get_attribute('innerHTML')

        soup = BeautifulSoup(html, 'html.parser')

        kids = soup.find('img',
                         src=re.compile(".*_familyPlans.*"))
        return kids['alt']
    except:
        return ""


def get_bio_star_sign(driver):
    try:
        parent_elem = driver.find_element(By.CLASS_NAME, PARENT_BUMBLE_CLASS_NAME)
        html = parent_elem.get_attribute('innerHTML')
        soup = BeautifulSoup(html, 'html.parser')
        sign = soup.find('img',
                         src=re.compile(".*_starSign.*"))
        return sign['alt']
    except:
        return ""


def get_bio_politics(driver):
    try:
        parent_elem = driver.find_element(By.CLASS_NAME, PARENT_BUMBLE_CLASS_NAME)

        html = parent_elem.get_attribute('innerHTML')

        soup = BeautifulSoup(html, 'html.parser')

        politics = soup.find('img',
                             src=re.compile(".*_Politics.*"))
        return politics['alt']
    except:
        return ""


def get_bio_religion(driver):
    try:
        parent_elem = driver.find_element(By.CLASS_NAME, PARENT_BUMBLE_CLASS_NAME)
        html = parent_elem.get_attribute('innerHTML')
        soup = BeautifulSoup(html, 'html.parser')
        religion = soup.find('img',
                             src=re.compile(".*_religion.*"))
        return religion['alt']
    except:
        return ""


def get_bio_about_me(driver):
    try:
        parent_elem = driver.find_element(By.CLASS_NAME, PARENT_BUMBLE_CLASS_NAME)
        html = parent_elem.get_attribute('innerHTML')
        soup = BeautifulSoup(html, 'html.parser')

        header = ((soup.find('section', 'encounters-story-section encounters-story-section--about')
                   .find('h2', "p-2 font-weight-medium"))
                  .next_element.text)
        text = ((soup.find('section', 'encounters-story-section encounters-story-section--about')
                 .find('p', "encounters-story-about__text"))
                .next_element.text)

        about_me = header + os.linesep + text

        return about_me
    except:
        return ""


def get_bio_sections(driver):
    try:
        parent_elem = driver.find_element(By.CLASS_NAME, PARENT_BUMBLE_CLASS_NAME)
        html = parent_elem.get_attribute('innerHTML')
        soup = BeautifulSoup(html, 'html.parser')

        sectionsElements = soup.find_all('section', 'encounters-story-section encounters-story-section--question')

        sections = []
        for section in sectionsElements:
            section_header = section.find('h2', "p-2 font-weight-medium").next_element.text
            section_text = section.find('p', "encounters-story-about__text").next_element.text
            sections.append(section_header + '\n' + section_text)

        return sections
    except:
        return []


def get_location_pills(driver):
    try:
        parent_elem = driver.find_element(By.CLASS_NAME, PARENT_BUMBLE_CLASS_NAME)

        html = parent_elem.get_attribute('innerHTML')

        soup = BeautifulSoup(html, 'html.parser')

        location_pills = soup.find_all('div', 'location-widget__info')

        return location_pills
    except:
        return []


def get_bio_current_location(driver):
    try:
        parent_elem = driver.find_element(By.CLASS_NAME, PARENT_BUMBLE_CLASS_NAME)
        html = parent_elem.get_attribute('innerHTML')
        soup = BeautifulSoup(html, 'html.parser')
        current_location = (soup.find('div', 'location-widget__town')
                            .find('span', 'header-2 text-color-black')).text
        return current_location
    except:
        return ""


def get_bio_lives_in_location(driver):
    try:
        parent_elem = get_location_pills(driver)[0]
        for elem in parent_elem:
            lives_in = (elem.find('div', 'p-3 text-ellipsis font-weight-medium')).text
            if lives_in.__contains__("Lives in"):
                lives_in = re.split(r'.*Lives in', lives_in)[1]
                return lives_in.strip(" ")
            else:
                continue
    except:
        return ""


def get_bio_city(driver):
    try:
        return get_bio_lives_in_location(driver).split(",")[0].strip(" ")
    except:
        return ""

def get_bio_state(driver):
    try:
        return get_bio_lives_in_location(driver).split(",")[1].strip(" ")
    except:
        return ""

def get_bio_from_location(driver):
    try:
        parent_elem = get_location_pills(driver)[0]
        for elem in parent_elem:
            from_location = (elem.find('div', 'p-3 text-ellipsis font-weight-medium')).text
            if from_location.__contains__("From"):
                from_location = re.split(r'.*From', from_location)[1]
                return from_location.strip(" ")
            else:
                continue
    except:
        return ""


def get_bio_locations(driver):
    try:
        locations = []
        locations.append(get_bio_current_location(driver))
        locations.append(get_bio_lives_in_location(driver))
        locations.append(get_bio_from_location(driver))
        return locations
    except:
        return []
