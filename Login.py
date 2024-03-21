import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.NAME,"email").send_keys("hello@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("123456")
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Manoj")
driver.find_element(By.ID,"exampleCheck1").click()

time.sleep(5)
driver.quit()
