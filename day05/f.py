"""Selenium WebDriver Login Test"""
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By

options = ChromeOptions()
options.binary_location = "D:/Apps/ungoogled-chromium-116.0.5845.141-2_Win64/chrome.exe"
driver = webdriver.Chrome(options=options)

driver.get("https://practicetestautomation.com/practice-test-login/")
email_field = driver.find_element(By.ID, "username")
email_field.send_keys("student")
pwd_field = driver.find_element(By.ID, "password")
pwd_field.send_keys("Password123")
submit_button = driver.find_element(By.ID, "submit")
submit_button.click()

driver.quit()
