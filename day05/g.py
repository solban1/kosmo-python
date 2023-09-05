"""Selenium WebDriver Google Images"""
import os
import time
import urllib.request
import requests

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = "https://www.google.com/imghp"

options = ChromeOptions()
options.binary_location = "D:/Apps/ungoogled-chromium-116.0.5845.141-2_Win64/chrome.exe"
driver = webdriver.Chrome(options=options)
driver.get(url)

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("test")
search_box.send_keys(Keys.ENTER)
driver.implicitly_wait(2)
imgs = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")
imgs[0].click()
img_original = driver.find_element(By.CSS_SELECTOR, ".r48jcc.pT0Scc.iPVvYb")
img_src = img_original.get_attribute("src")
assert isinstance(img_src, str)
print(img_src)
driver.quit()

download_dir = "D:/Sol/tmp/downloads"
if not os.path.exists(download_dir):
    os.makedirs(download_dir)


urllib.request.urlretrieve(img_src, download_dir + "/test.jpg")
requests.get(
    img_src,
)
