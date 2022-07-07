import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select

s=Service(executable_path="C:\\Users\\91959\\Downloads\\chromedriver_win32 (2)\\chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("http://www.fb.com")
driver.maximize_window()
driver.implicitly_wait(30)
actual_title=driver.title
print(actual_title)
actual_url=driver.current_url
print(actual_url)
driver.swithch_to.alert.accept()
driver.find_element(By.XPATH,"//a[starts-with(@id,'u_0_2')]").click()
month_drop=driver.find_element(By.ID,"month")
sel=Select(month_drop)
time.sleep(3)
sel.select_by_visible_text("Aug")
time.sleep(3)
sel.select_by_value("10")
time.sleep(3)
sel.select_by_index(1)
driver.close()
