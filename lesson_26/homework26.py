from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

driver = Chrome()
driver.get("http://localhost:8000/dz.html")

driver.switch_to.frame(driver.find_element(By.ID, "frame1"))
frame1_field = driver.find_element(By.ID, "input1")
frame1_field.send_keys("Frame1_Secret")
check_button1 = driver.find_element(By.CSS_SELECTOR, "button[onclick=\"verifyInput('input1')\"]")
check_button1.click()

alert = Alert(driver)
alert.accept()

driver.switch_to.default_content()

driver.switch_to.frame(driver.find_element(By.ID, "frame2"))
frame2_field = driver.find_element(By.ID, "input2")
frame2_field.send_keys("Frame2_Secret")
check_button2 = driver.find_element(By.CSS_SELECTOR, "button[onclick=\"verifyInput('input2')\"]")
check_button2.click()
alert = Alert(driver)
alert.accept()

driver.quit()

