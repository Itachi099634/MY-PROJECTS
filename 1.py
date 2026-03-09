from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.opera()
driver.get("https://web.whatsapp.com")

input("Scan QR code and press Enter")

# open chat
driver.get("https://web.whatsapp.com/send?phone=918178886307&text=Hello")

time.sleep(10)

send = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
send.click()
