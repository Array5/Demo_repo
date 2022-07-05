import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s=Service(executable_path="C:\\Users\\91959\\Downloads\\chromedriver_win32 (2)\\chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("http://www.fb.com")
driver.maximize_window()
diver.close()
