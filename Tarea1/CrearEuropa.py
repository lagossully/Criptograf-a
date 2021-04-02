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
driver.find_element_by_name('sibbo-cmp-button sibbo-cmp-button--xl').click()
time.sleep(10)
driver.find_element_by_class_name('login').click()
time.sleep(10)
driver.find_element_by_xpath('login-page__link').click()
time.sleep(10)
driver.find_element_by_name('email').send_keys('seba.piniera@gmail.com')
time.sleep(2)
driver.find_element_by_name('register-container__form__button').click()
time.sleep(10)
driver.find_element_by_id('name').send_keys('Fernando')
time.sleep(2)
driver.find_element_by_name('lastName').send_keys('García')
time.sleep(2)
driver.find_element_by_name('nick').send_keys('sebapiniera')
time.sleep(2)
driver.find_element_by_name('password').send_keys('HoL1Qu3T4l')
time.sleep(2)
driver.find_element_by_class_name('register-container__form__button').click()
time.sleep(10)
driver.quit()