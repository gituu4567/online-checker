import pickle
import selenium.webdriver 
import time

driver = selenium.webdriver.Chrome("driver/chromedriver")
driver.get("https://web.whatsapp.com/")

raw_input("Press enter to dump cookies")


pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
print "dump successful"