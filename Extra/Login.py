import pickle
from Config import EdgeConfig
from Config.Config import COOKIES_DIR, BUMBLE_WEBSITE

driver = EdgeConfig.configure_edge()
driver.get(BUMBLE_WEBSITE)

print("Press Enter to continue...")
input()

cookies = driver.get_cookies()
pickle.dump(cookies, open("../"+COOKIES_DIR, "wb"))
