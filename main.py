# This is a sample Python script.
from time import sleep

from Edge import EdgeCommands
from Bumble import BumbleScrapeTools

des = "images\\"
attributes = {'class': 'encounters-album__stories-container'}
parentBumbleBioElement_XPATH = '//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[1]/article/div[1]'


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
# def download_images_from_bio():
#     parentElem = driver.find_element(By.XPATH, parentBumbleBioElement_XPATH)
#     src_list = BumbleScrapeTools.get_list_of_src_from_element(parentElem)
#     BumbleScrapeTools.download_images_from_src(src_list, des)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    driver = EdgeCommands.nav_to_bumble()
    sleep(3)

    BumbleScrapeTools.download_images_from_bio(driver, des)

    driver.close()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
