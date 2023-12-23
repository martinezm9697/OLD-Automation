import os
import requests
import re

from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

from config import PARENT_BUMBLE_BIO_XPATH, PARENT_BUMBLE_CLASS_NAME


def get_list_of_src_from_element(element):
    html = element.get_attribute('innerHTML')

    soup = BeautifulSoup(html, 'html.parser')

    elem_list = soup.find_all('img', 'media-box__picture-image')

    for i in range(len(elem_list)):
        elem_list[i] = elem_list[i]['src']

    return (elem_list)


def download_images_from_src(src_list, destination):
    for i, src in enumerate(src_list):
        # Get the URL of the image
        image_url = 'http:' + src

        # Check if the directory exists
        if not os.path.exists(destination):
            # If the directory doesn't exist, create it
            os.makedirs(destination)

        # Send a GET request to the image URL
        r = requests.get(image_url, stream=True)
        if r.status_code == 200:
            # If the GET request is successful, the status code will be 200
            with open(os.path.join(destination, 'image{}.jpg'.format(i)), 'wb') as f:
                f.write(r.content)


def download_images_from_bio(driver, des):
    parent_elem = driver.find_element(By.CLASS_NAME, PARENT_BUMBLE_CLASS_NAME)
    src_list = get_list_of_src_from_element(parent_elem)
    download_images_from_src(src_list, des)


def get_bio_name(driver):
    name = driver.find_element(By.CLASS_NAME, 'encounters-story-profile__name')
    return name.text


def get_bio_age(driver):
    age = driver.find_element(By.CLASS_NAME, 'encounters-story-profile__age')
    return re.split(r',', age.text)[1].strip(" ")


def get_photo_verified(driver):
    photo_verified = driver.find_element(By.CLASS_NAME, 'encounters-story-profile__verification-badge')
    if photo_verified:
        return True


def get_badges(driver):
    parent_elem = driver.find_element(By.CLASS_NAME, PARENT_BUMBLE_CLASS_NAME)

    html = parent_elem.get_attribute('innerHTML')
    soup = BeautifulSoup(html, 'html.parser')

    badges_child_elements = (soup.find('ul', 'encounters-story-about__badges')
                             .find_all('li', 'encounters-story-about__badge'))

    badges = []
    for badge in badges_child_elements:
        badges.append(badge.text)
    return badges


def get_bio_height(driver):
    parent_elem = driver.find_element(By.CLASS_NAME, PARENT_BUMBLE_CLASS_NAME)

    html = parent_elem.get_attribute('innerHTML')

    soup = BeautifulSoup(html, 'html.parser')

    height = soup.find('img',
                       src=re.compile(".*_height.*"))

    return height['alt']


def get_bio_occupation(driver):
    parent_elem = driver.find_element(By.CLASS_NAME, PARENT_BUMBLE_CLASS_NAME)
    html = parent_elem.get_attribute('innerHTML')
    soup = BeautifulSoup(html, 'html.parser')
    occupation = soup.find('p', 'encounters-story-profile__occupation')
    return occupation.text


def get_bio_school(driver):
    parent_elem = driver.find_element(By.CLASS_NAME, PARENT_BUMBLE_CLASS_NAME)
    html = parent_elem.get_attribute('innerHTML')
    soup = BeautifulSoup(html, 'html.parser')
    school = soup.find('p', 'encounters-story-profile__education')
    return school.text


def get_bio_exercise(driver):
    parent_elem = driver.find_element(By.CLASS_NAME, PARENT_BUMBLE_CLASS_NAME)

    html = parent_elem.get_attribute('innerHTML')

    soup = BeautifulSoup(html, 'html.parser')

    exercise = soup.find('img',
                         src=re.compile(".*_exercise.*"))
    return exercise['alt']


def get_bio_education(driver):
    parent_elem = driver.find_element(By.CLASS_NAME, PARENT_BUMBLE_CLASS_NAME)

    html = parent_elem.get_attribute('innerHTML')

    soup = BeautifulSoup(html, 'html.parser')

    education = soup.find('img',
                          src=re.compile(".*_education.*"))
    return education['alt']


def get_bio_drinking(driver):
    parent_elem = driver.find_element(By.CLASS_NAME, PARENT_BUMBLE_CLASS_NAME)

    html = parent_elem.get_attribute('innerHTML')

    soup = BeautifulSoup(html, 'html.parser')

    drinking = soup.find('img',
                         src=re.compile(".*_drinking.*"))
    return drinking['alt']


def get_bio_smoking(driver):
    parent_elem = driver.find_element(By.CLASS_NAME, PARENT_BUMBLE_CLASS_NAME)

    html = parent_elem.get_attribute('innerHTML')

    soup = BeautifulSoup(html, 'html.parser')

    smoking = soup.find('img',
                        src=re.compile(".*_smoking.*"))
    return smoking['alt']


def get_bio_gender(driver):
    parent_elem = driver.find_element(By.CLASS_NAME, PARENT_BUMBLE_CLASS_NAME)

    html = parent_elem.get_attribute('innerHTML')

    soup = BeautifulSoup(html, 'html.parser')

    politics = soup.find('img',
                         src=re.compile(".*_gender.*"))
    return politics['alt']


def get_bio_intentions(driver):
    parent_elem = driver.find_element(By.CLASS_NAME, PARENT_BUMBLE_CLASS_NAME)
    html = parent_elem.get_attribute('innerHTML')
    soup = BeautifulSoup(html, 'html.parser')
    dating_intentions = soup.find('img',
                                  src=re.compile(".*_intentions.*"))
    return dating_intentions['alt']


def get_bio_family_plans(driver):
    parent_elem = driver.find_element(By.CLASS_NAME, PARENT_BUMBLE_CLASS_NAME)

    html = parent_elem.get_attribute('innerHTML')

    soup = BeautifulSoup(html, 'html.parser')

    kids = soup.find('img',
                     src=re.compile(".*_familyPlans.*"))
    return kids['alt']


def get_bio_star_sign(driver):
    parent_elem = driver.find_element(By.CLASS_NAME, PARENT_BUMBLE_CLASS_NAME)
    html = parent_elem.get_attribute('innerHTML')
    soup = BeautifulSoup(html, 'html.parser')
    sign = soup.find('img',
                     src=re.compile(".*_starSign.*"))
    return sign['alt']


def get_bio_politics(driver):
    parent_elem = driver.find_element(By.CLASS_NAME, PARENT_BUMBLE_CLASS_NAME)

    html = parent_elem.get_attribute('innerHTML')

    soup = BeautifulSoup(html, 'html.parser')

    politics = soup.find('img',
                         src=re.compile(".*_Politics.*"))
    return politics['alt']


def get_bio_religion(driver):
    parent_elem = driver.find_element(By.CLASS_NAME, PARENT_BUMBLE_CLASS_NAME)
    html = parent_elem.get_attribute('innerHTML')
    soup = BeautifulSoup(html, 'html.parser')
    religion = soup.find('img',
                         src=re.compile(".*_religion.*"))
    return religion['alt']


def get_bio_about_me(driver):
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


def get_bio_sections(driver):
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


def get_location_pills(driver):
    parent_elem = driver.find_element(By.CLASS_NAME, PARENT_BUMBLE_CLASS_NAME)

    html = parent_elem.get_attribute('innerHTML')

    soup = BeautifulSoup(html, 'html.parser')

    location_pills = soup.find_all('div', 'location-widget__info')

    return location_pills


def get_bio_current_location(driver):
    parent_elem = driver.find_element(By.CLASS_NAME, PARENT_BUMBLE_CLASS_NAME)
    html = parent_elem.get_attribute('innerHTML')
    soup = BeautifulSoup(html, 'html.parser')
    current_location = (soup.find('div', 'location-widget__town')
                        .find('span', 'header-2 text-color-black')).text
    return current_location


def get_bio_lives_in_location(driver):
    parent_elem = driver.find_element(By.CLASS_NAME, PARENT_BUMBLE_CLASS_NAME)
    parent_elem = get_location_pills(driver)[0]
    for elem in parent_elem:
        lives_in = (elem.find('div', 'p-3 text-ellipsis font-weight-medium')).text
        if lives_in.__contains__("Lives in"):
            lives_in = re.split(r'.*Lives in', lives_in)[1]
            return lives_in.strip(" ")
        else:
            continue


def get_bio_city(driver):
    return get_bio_lives_in_location(driver).split(",")[0].strip(" ")


def get_bio_state(driver):
    return get_bio_lives_in_location(driver).split(",")[1].strip(" ")


def get_bio_from_location(driver):
    parent_elem = get_location_pills(driver)[0]
    for elem in parent_elem:
        from_location = (elem.find('div', 'p-3 text-ellipsis font-weight-medium')).text
        if from_location.__contains__("From"):
            from_location = re.split(r'.*From', from_location)[1]
            return from_location.strip(" ")
        else:
            continue


def get_bio_locations(driver):
    locations = []
    locations.append(get_bio_current_location(driver))
    locations.append(get_bio_lives_in_location(driver))
    locations.append(get_bio_from_location(driver))
    return locations
