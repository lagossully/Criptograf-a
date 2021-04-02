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
driver.find_element_by_class_name('icon-new icon-user').click()
time.sleep(10)
driver.find_element_by_name('spree_user[first_name]').send_keys('Fernando')
time.sleep(2)
driver.find_element_by_class_name('spree_user[last_name_father]').send_keys('García')
time.sleep(2)
driver.find_element_by_class_name('spree_user[last_name_mother]').send_keys('Morales')
time.sleep(2)
driver.find_element_by_name('email').send_keys('seba.piniera@gmail.com')
time.sleep(2)
driver.find_element_by_name('spree_user[rut]').send_keys('7.284.965-5')
time.sleep(2)
driver.find_element_by_name('spree_user[gender]').select_by_visible_text('Masculino')
time.sleep(2)
driver.find_element_by_name('spree_user[birthday(3i)]').select_by_visible_text('15')
time.sleep(2)
driver.find_element_by_name('spree_user[birthday(2i)]').select_by_visible_text('Mayo')
time.sleep(2)
driver.find_element_by_name('spree_user[birthday(1i)]').select_by_visible_text('2001')
time.sleep(2)
driver.find_element_by_name('spree_user[phone_number]').send_keys('98436662')
time.sleep(2)
driver.find_element_by_name('spree_user[email]').send_keys('seba.piniera@gmail.com')
time.sleep(2)
driver.find_element_by_name('spree_user[email_confirmation]').send_keys('seba.piniera@gmail.com')
time.sleep(2)
driver.find_element_by_name('spree_user[password]').send_keys('HoL1Qu3T4l!')
time.sleep(2)
driver.find_element_by_name('sb-terms-conditions').click()
time.sleep(2)
driver.find_element_by_name('sb-terms-conditions').click()
time.sleep(10)
driver.find_element_by_name('commit').click()
time.sleep(10)
driver.quit()
