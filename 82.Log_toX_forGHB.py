#Base:
#import wait as wait
from selenium import webdriver
cService = webdriver.ChromeService(executable_path='/home/sandy/Downloads/chromedriver')
from selenium.webdriver.common.by import By
#import pandas as pd
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

options = webdriver.ChromeOptions()
#options.add_argument("--headless=new")
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service = cService, options=options)

#Code
random_integer = random.randint(2, 6)
web = 'https://x.com'
driver.get(web)

login = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//a[@href='/login']"))
)
time.sleep(random_integer)
login.click()
# Find username Field

