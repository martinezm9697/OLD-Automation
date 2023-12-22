import os
from time import sleep

import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

from Edge import EdgeCommands


def get_list_of_src_from_element(element):
    html = element.get_attribute('innerHTML')

    soup = BeautifulSoup(html, 'html.parser')

    elem_list = soup.find_all('img', 'media-box__picture-image')

    for i in range(len(elem_list)):
        elem_list[i] = elem_list[i]['src']

    return(elem_list)



driver = EdgeCommands.nav_to_bumble()
sleep(5)
parentBumbleBioElement = driver.find_element(By.XPATH,
                                             '//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[1]/article/div[1]')
src_list = get_list_of_src_from_element(parentBumbleBioElement)


for i, src in enumerate(src_list):
    # Get the URL of the image
    image_url = 'http:' + src

    # Send a GET request to the image URL
    r = requests.get(image_url, stream=True)
    if r.status_code == 200:
        # If the GET request is successful, the status code will be 200
        with open(os.path.join('../images', 'image{}.jpg'.format(i)), 'wb') as f:
            f.write(r.content)

