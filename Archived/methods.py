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