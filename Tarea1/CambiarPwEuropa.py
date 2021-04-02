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
driver.find_element_by_name('password').send_keys('HoL1Qu3T4l')
time.sleep(2)
driver.find_element_by_class_name('login__button').click()
time.sleep(10)
driver.find_element_by_class_name('user').click()
time.sleep(2)
driver.find_element_by_class_name('login-user').click()
time.sleep(2)
driver.find_element_by_class_name('change__password').click()
time.sleep(10)
driver.find_element_by_name('currentPassword').send_keys('HoL1Qu3T4l')
time.sleep(2)
driver.find_element_by_name('newPassword').send_keys('H0L1Qu3T4l')
time.sleep(2)
driver.find_element_by_class_name('profile-account__form-save').click()
time.sleep(10)
driver.quit()

