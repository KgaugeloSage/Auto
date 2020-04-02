from selenium import webdriver

import time

driver = webdriver.Chrome()

driver.get(' https://forms.gle/E2W9cC5cpHQdu1EL7') 

driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys('name.surname@umuzi.org')

driver.find_element_by_xpath('//*[@id="identifierNext"]/span/span').click()

time.sleep(4)

driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys('password')

driver.find_element_by_xpath('//*[@id="passwordNext"]/span').click()

time.sleep(4)

driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[1]/div/div[2]/div/span/div/div[4]/label/div/div[1]/div/div[3]/div').click()

time.sleep(4)

driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[2]/div/div[2]/div/span/div/div[4]/label/div/div[1]/div/div[3]/div').click()

time.sleep(4)

driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/textarea').send_keys('Syllabus work')

time.sleep(4)

driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[4]/div/div[2]/div[1]/div[2]/textarea').send_keys('No challenges. Am good Thanks')

time.sleep(4)

driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[5]/div/div[2]/div/span/div/div[3]/label/div/div[1]/div/div[3]/div').click()

