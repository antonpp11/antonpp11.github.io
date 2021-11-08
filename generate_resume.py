from selenium import webdriver
import time

driver = webdriver.Chrome('~/Downloads/chromedriver')
# driver = webdriver.Chrome(DRIVER)
time.sleep(5)
driver.get('https://antonpp11.github.io/about.html')
screenshot = driver.save_screenshot('~/Downloads/my_screenshot.png')
driver.quit()