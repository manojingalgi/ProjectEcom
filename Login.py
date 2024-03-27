import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com/angularpractice")
driver.find_element(By.XPATH, "(//input[@name='name'])[1]").send_keys("Manoj Kulkarni")
driver.find_element(By.NAME,"email").send_keys("hello@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("123456")
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Manoj")
time.sleep(1)
driver.find_element(By.ID,"exampleCheck1").click()
#for dropdown
dropdown= Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Male")
print("beforeloop")
radiobuttons = driver.find_elements(By.XPATH, "//input[@type='radio']")
for radiobutton in radiobuttons:
    if radiobutton.is_displayed():
       radiobutton.get_attribute("value") == "Employed"
       radiobutton.click()
       print("Employed radio button clicked")
       break  # If you only want to click the first "Employed" radio button, you can break out of the loop here
else:
    print("Employed radio button not found")

driver.find_element(By.XPATH,"//input[@type='submit']").click()
# //input[@div='alert alert-success alert-dismissible']
msg = driver.find_element(By.CLASS_NAME,"alert-success").text

driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("You are working hard Manoj , Carry on")
print(msg)

assert "Success" in msg
time.sleep(3)
