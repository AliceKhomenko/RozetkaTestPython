from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os



dirpath = os.getcwd()
print("current directory is : " + dirpath)

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(executable_path=dirpath+"/drivers/chromedriver.exe",chrome_options=options)
driver.get("http://rozetka.com.ua")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found."  in driver.page_source
driver.close()