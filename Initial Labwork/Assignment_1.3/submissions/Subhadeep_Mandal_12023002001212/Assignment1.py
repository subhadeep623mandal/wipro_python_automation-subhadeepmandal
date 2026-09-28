# #1. Web Element Identification

import time  # Used to add a delay in the program

from selenium import webdriver  # Used to launch and control the browser
from selenium.webdriver.common.by import By  # Used to specify different locator strategies

driver = webdriver.Edge()  # Opens the Microsoft Edge browser

driver.get("https://rahulshettyacademy.com/angularpractice/")  # Opens the given webpage

name = driver.find_element(By.NAME, "name")  # Finds the Name input field using the NAME locator

name.send_keys("Subhadeep")  # Enters "Subhadeep" into the Name field

password = driver.find_element(By.ID, "exampleInputPassword1")  # Finds the password field using its ID

password.send_keys("1234")  # Enters "1234" into the password field

inputs = driver.find_elements(By.TAG_NAME, "input")  # Finds all input elements using the TAG_NAME locator

print("Total inputs:", len(inputs))  # Prints the total number of input elements

checkbox = driver.find_element(By.CLASS_NAME, "form-check-input")  # Finds the checkbox using CLASS_NAME

checkbox.click()  # Clicks the checkbox

time.sleep(2)  # Waits for 2 seconds

link = driver.find_element(By.LINK_TEXT, "Shop")  # Finds the Shop link using LINK_TEXT

link.click()  # Clicks the Shop link

time.sleep(2)  # Waits for 2 seconds