"""Selenium WebDriver Tutorial"""
from selenium import webdriver
from selenium.webdriver import ChromeOptions

options = ChromeOptions()
options.binary_location = "D:/Apps/ungoogled-chromium-116.0.5845.141-2_Win64/chrome.exe"
driver = webdriver.Chrome(options=options)
print(driver.capabilities)

driver.get("https://google.com/ncr")
search_box = driver.find_element("name", "q")
print(search_box)


driver.quit()
