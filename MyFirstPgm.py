import time

from selenium import webdriver
from selenium.webdriver.opera.service import Service

s=Service(executable_path="C:\\Users\\91959\\Downloads\\chromedriver_win32 (2)\\operadriver.exe")
driver=webdriver.Opera(service=s)
driver.get("http://www.fb.com")
driver.maximize_window()
actual_title=driver.title
print(actual_title)
actual_url=driver.current_url
print(actual_url)
diver.close()
