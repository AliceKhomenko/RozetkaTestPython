from datetime import datetime

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

import os
import time

from selenium.webdriver.support.wait import WebDriverWait

from test.custom_waits.number_of_elements_more_than import number_of_element_more_than

ROOT_DIR = os.path.abspath(os.curdir)
print(ROOT_DIR)
dirpath = os.getcwd()
print("current directory is : " + dirpath)

options = webdriver.ChromeOptions()
options.add_argument('window-size=1920x1080')
options.add_argument("--start-maximized")

# options.add_argument('headless')
driver = webdriver.Chrome(executable_path=dirpath + "/drivers/chromedriver.exe", chrome_options=options)
try:
    driver.get("http://rozetka.com.ua")
    elem = driver.find_element_by_xpath(
        "//a[@class='menu-categories__link' and contains(text(),'Ноутбуки и компьютеры')]")
    ActionChains(driver).move_to_element(elem).perform()
    time.sleep(1)
    elem = driver.find_element_by_xpath("//a[@class='menu__hidden-title'  and contains(text(),'Ноутбуки')]")
    wait = WebDriverWait(driver, 5)
    wait.until(EC.visibility_of(elem))
    elem.click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "img[title='Ноутбуки с SSD']")))
    elem = driver.find_element_by_css_selector("img[title='Ноутбуки с SSD']")
    elem.click()
    elems = driver.find_elements_by_name("goods_item_with_promotion")
    ActionChains(driver).move_to_element(elems[0]).perform()
    driver.implicitly_wait(10)
    time.sleep(5)
    # wait.until(EC.visibility_of(elems[0].find_element_by_class_name("short-description")))
    compare_button = elems[0].find_element_by_xpath("//img[starts-with(@alt,'Добавить к')]")
    compare_button.click()
    ActionChains(driver).move_to_element(elems[1]).perform()
    compare_button = elems[1].find_element_by_xpath("//img[starts-with(@alt,'Добавить к')]")
    compare_button.click()
    wait.until(number_of_element_more_than((By.XPATH, "//img[starts-with(@alt,'Добавлено к')]"), 1))
    elem = driver.find_element_by_xpath("//*[text()='Сравнение']")
    elem.click()
    elem = driver.find_element_by_xpath("//*[text()='Сравнить эти товары']")
    elem.click()
    if (len(elems)) > 1:
        print()
    elems = driver.find_elements_by_xpath("//*[@class='comparison-t-row']")
    count = 0
    for row in elems:
        list = []
        for e in row.find_elements_by_class_name("chars-value-inner"):
            list.append(e.text)
        s = set(list)
        print(s)
        if (len(s)) > 1:
            count += 1
        print(count)
    print("count=", count)
    elem = driver.find_element_by_xpath("//*[contains(text(),'Только отличия')]")
    elem.click()
    time.sleep(2)
    elems = driver.find_elements_by_xpath("//*[@class='comparison-t-row']")
    new_count = 0
    for rows in elems:
        if rows.is_displayed():
            new_count += 1
    print("new count=", new_count)
    assert count == new_count
except Exception as e:
    print(e)
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    driver.get_screenshot_as_file('screenshot-%s.png' % now)
finally:
    driver.quit()
