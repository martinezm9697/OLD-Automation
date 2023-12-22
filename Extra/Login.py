import pickle
from Edge import EdgeConfig
from config import COOKIES_DIR, BUMBLE_WEBSITE

driver = EdgeConfig.configure_edge()
driver.get(BUMBLE_WEBSITE)

print("Press Enter to continue...")
input()

cookies = driver.get_cookies()
pickle.dump(cookies, open(COOKIES_DIR, "wb"))
