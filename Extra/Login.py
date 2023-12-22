import pickle
from Edge import EdgeConfig

driver = EdgeConfig.configure_edge()
driver.get("https://www.bumble.com/")

print("Press Enter to continue...")
input()

cookies = driver.get_cookies()
pickle.dump(cookies, open("../cookies.pkl", "wb"))
