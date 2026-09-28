# 2. Multiple Element Identification

import time  # Used to add delays in the program

from selenium import webdriver  # Used to launch and control the browser
from selenium.webdriver.common.by import By  # Used for different locator strategies

driver = webdriver.Edge()  # Opens the Microsoft Edge browser

driver.get("https://rahulshettyacademy.com/angularpractice/")  # Opens the given webpage

links = driver.find_elements(By.TAG_NAME, "a")  # Finds all <a> (anchor/link) elements on the page

for link in links:  # Loops through each link found on the webpage
    print(link.text)  # Prints the visible text of each link