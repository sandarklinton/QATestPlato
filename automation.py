from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time 

driver = webdriver.Chrome()
driver.set_page_load_timeout(20)
driver.implicitly_wait(20)

driver.get('https://en-gb.facebook.com/reg/')

driver.find_element(By.XPATH, '//div[@class=\'placeholder\']/following-sibling::input').send_keys('Sandar')

driver.find_element(By.XPATH, '//input[@aria-label=\'Surname\']').send_keys('Klinton')

driver.find_element(By.XPATH, '//input[@aria-label=\'Mobile number or email address\']').send_keys('sandarklinton@gmail.com')

driver.find_element(By.XPATH, '//input[@aria-label=\'Re-enter email address\']').send_keys('sandarklinton@gmail.com')

driver.find_element(By.XPATH, '//input[@aria-label=\'New password\']').send_keys('newpassword')

Select(driver.find_element(By.XPATH, '//select[@aria-label=\'Day\']')).select_by_visible_text('24')
Select(driver.find_element(By.XPATH, '//select[@aria-label=\'Month\']')).select_by_visible_text('Jan')
Select(driver.find_element(By.XPATH, '//select[@aria-label=\'Year\']')).select_by_visible_text('1995')

driver.find_element(By.XPATH, '//input[@type=\'radio\'][@value=2]').click()
time.sleep(10)
