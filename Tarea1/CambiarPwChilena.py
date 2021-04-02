import os
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import io
import random

driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.salcobrand.cl/')

time.sleep(30)
driver.find_element_by_class_name('user-options-content').click()
time.sleep(10)
driver.find_element_by_name('spree_user[email]').send_keys('seba.piniera@gmail.com')
time.sleep(2)
driver.find_element_by_name('spree_user[password]').send_keys('HoL1Qu3T4l!')
time.sleep(2)
driver.find_element_by_class_name('btn btn-flat').click()
time.sleep(10)
driver.find_element_by_class_name('user-options-content').click()
time.sleep(10)
driver.find_element_by_class_name('login__form-recover').click()
time.sleep(10)
driver.find_element_by_name('spree_user[password]').send_keys('HoL1Qu3T4l!')
driver.sleep(2)
driver.find_element_by_name('spree_user[new_password]').send_keys('H0L1Qu3T4l!')
driver.sleep(2)
driver.find_element_by_name('spree_user[new_password_confirmation]').send_keys('H0L1Qu3T4l!')
driver.sleep(10)
driver.quit()