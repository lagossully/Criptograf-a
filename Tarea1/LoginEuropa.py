import os
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import io
import random

driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.eldiario.es/')

time.sleep(30)
driver.find_element_by_class_name('login').click()
time.sleep(10)
driver.find_element_by_name('email').send_keys('seba.piniera@gmail.com')
time.sleep(2)
driver.find_element_by_name('password').send_keys('HoL1Qu3T4l')
time.sleep(2)
driver.find_element_by_class_name('login__button').click()
time.sleep(10)
driver.quit()