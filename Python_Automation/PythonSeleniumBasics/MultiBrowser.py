from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(
    executable_path="C://Pranay//PythonWorkspace//Python_Automation//Driver//chromedriver_win32//chromedriver.exe")

driver.get("http://demo.guru99.com/test/newtours/")

print(driver.title)  # Title of the page

driver.quit()
