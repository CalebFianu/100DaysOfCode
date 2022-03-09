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

driver.get("https://www.rottentomatoes.com")
print("This website is called: " + driver.title)

search = driver.find_element_by_class_name("search-text")
search.send_keys("the matrix")
search.send_keys(Keys.RETURN)

driver.implicitly_wait(20)

# link = driver.find_element_by_link_text("The Matrix Reloaded")
# link.click()


rating = WebDriverWait(driver, 20).until(
    ec.element_to_be_clickable((By.XPATH, "//img[@src='https://resizing.flixster.com/6UHQX0XXTHsWAgnapGOSE3NslW4=/fit-in/80x126/v2/https://flxt.tmsimg.com/assets/p22804_p_v10_ab.jpg']"))).click()




# for rating in driver.find_elements_by_xpath('.//span[@data-qa="tomatometer"]'):
#     print(rating.text)