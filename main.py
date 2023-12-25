from time import sleep

from Bumble.BumbleAutomation import rate_bios_until_end
from Edge import EdgeCommands

if __name__ == '__main__':
    print('OLD Automation Started')

    driver = EdgeCommands.nav_to_bumble()
    sleep(3)

    rate_bios_until_end(driver)

    driver.close()

    print('OLD Automation Finished')


