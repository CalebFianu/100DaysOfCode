import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time


PATH = "C:\Program Files (x86)\chromedriver.exe"
os.environ['PATH'] += r"C:/Program Files (x86)/chromedriver.exe"
driver = webdriver.Chrome(PATH)
url = "www.youtube.com"
driver.get("https://www.imdb.com")
print("This website is called: " + driver.title)

search = driver.find_element_by_id("suggestion-search")
search.send_keys("the matrix")
search.send_keys(Keys.RETURN)

link = driver.find_element_by_link_text("The Matrix")
link.click()

for rating in driver.find_elements_by_xpath('.//span[@class = "AggregateRatingButton__RatingScore-sc-1ll29m0-1 iTLWoV"]'):
        print("This movie is rated " + rating.text + "/10.")



time.sleep(180)
driver.quit()



