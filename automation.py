from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import time 


#This test is designed for 'Sign up with invalid email' test case.
driver = webdriver.Chrome()
driver.set_page_load_timeout(20)
driver.implicitly_wait(20)

driver.get('https://en-gb.facebook.com/reg/')

driver.find_element(By.XPATH, '//div[@class=\'placeholder\']/following-sibling::input').send_keys('Sandar')

driver.find_element(By.XPATH, '//input[@aria-label=\'Surname\']').send_keys('Klinton')

driver.find_element(By.XPATH, '//input[@aria-label=\'Mobile number or email address\']').send_keys('asda@asdas.as')

driver.find_element(By.XPATH, '//input[@aria-label=\'Re-enter email address\']').send_keys('asda@asdas.as')

driver.find_element(By.XPATH, '//input[@aria-label=\'New password\']').send_keys('newpassword')

Select(driver.find_element(By.XPATH, '//select[@aria-label=\'Day\']')).select_by_visible_text('24')
Select(driver.find_element(By.XPATH, '//select[@aria-label=\'Month\']')).select_by_visible_text('Jan')
Select(driver.find_element(By.XPATH, '//select[@aria-label=\'Year\']')).select_by_visible_text('1995')

driver.find_element(By.XPATH, '//input[@type=\'radio\'][@value=2]').click()
driver.find_element(By.XPATH, '//button[@type=\'submit\']').click()
time.sleep(10)

WebDriverWait(driver, 50).until(
    expected_conditions.text_to_be_present_in_element((By.ID, 'reg_error_inner'), 'It looks like you may have entered an incorrect email address. Please correct it if necessary, then click to continue.'))
assert "It looks like you may have entered an incorrect email address. Please correct it if necessary, then click to continue." in driver.page_source
