import os
import urllib

import requests
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from config import PARENT_BUMBLE_BIO_XPATH


def find_image(driver, xpath):
    # Find the image using the full XPath
    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )

        image = driver.find_element(By.XPATH, xpath)

        # Get the 'src' attribute of the image
        src = image.get_attribute('src')
        return src
    except:
        print("Error finding image")
        driver.quit()


# 'encounters-album__stories-container'
def get_child_elements(html, attributes):
    # Parse the HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Find the parent element
    parent = soup.find('div', attrs=attributes)

    # Find all child elements
    children = parent.findChildren(recursive=True)

    return children


def get_images_src_from_html(html):
    # Parse the HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Find all img elements
    img_elements = soup.find_all('img')

    # Get the source URLs of the images
    img_sources = [img['src'] for img in img_elements]

    # Print the source URLs
    for src in img_sources:
        print(src)

    return img_sources


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
    parent_elem = driver.find_element(By.XPATH, PARENT_BUMBLE_BIO_XPATH)
    src_list = get_list_of_src_from_element(parent_elem)
    download_images_from_src(src_list, des)
