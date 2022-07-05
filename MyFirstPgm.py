import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service

s=Service(executable_path="C:\\Users\\91959\\Downloads\\chromedriver_win32 (2)\\msedgedriver.exe")
driver=webdriver.Edge(service=s)
driver.get("http://www.fb.com")
driver.maximize_window()
diver.close()
