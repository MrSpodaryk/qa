from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://google.com')

input_text = 'Flowers'

input_element = driver.find_element(By.XPATH, '//*[@class="gLFyf gsfi"]')
input_element.send_keys(input_text)

time.sleep(1)

driver.find_element(By.XPATH, '//*[@class="gNO89b"]').click()

time.sleep(1)

text_from_search = driver.find_element(By.XPATH, '//*[@class="gLFyf gsfi"]').get_attribute("value")

print(text_from_search == input_text)
