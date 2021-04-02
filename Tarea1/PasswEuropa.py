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
driver.find_element_by_class_name('login__forgot-password').click()
time.sleep(2)
driver.find_element_by_class_name('email-form-field__input').send_keys('seba.piniera@gmail.com')
time.sleep(2)
driver.find_element_by_class_name('forgot-password__button').click()
time.sleep(10)
driver.quit()
#se debe reestablecer desde el mail