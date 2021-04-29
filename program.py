from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#s = Service("C:\Program Files\Google\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome("C:\Program Files\Google\chromedriver_win32\chromedriver.exe")
driver.maximize_window()

driver.get("https://www.google.com/")
myPageTitle = driver.title
print(myPageTitle)
assert "Google" in myPageTitle
driver.quit()