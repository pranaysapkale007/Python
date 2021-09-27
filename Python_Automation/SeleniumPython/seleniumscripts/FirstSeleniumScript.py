from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Pranay\\PythonWorkspace\\Python_Automation\\Driver\\chromedriver_win32"
                                          "\\chromedriver.exe")

driver.get("http://www.google.com")
driver.maximize_window()

myPageTitle = driver.title

print(myPageTitle)

assert "Google" in myPageTitle

driver.quit()
