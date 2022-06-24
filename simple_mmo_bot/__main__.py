from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def main():
    driver = get_driver()
    driver.get("https://web.simple-mmo.com/login")
    assert "SimpleMMO" in driver.title
    login(driver)
    travel(driver)
    take_step(driver)

def login(driver):
    element = driver.find_element(By.NAME, "email")
    element.clear()
    element.send_keys("...")
    element = driver.find_element(By.NAME, "password")
    element.clear()
    element.send_keys("...")
    element.send_keys(Keys.RETURN)

def get_driver():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(chrome_options=chrome_options)
    return driver
    # assert "No results found." not in driver.page_source
    # driver.close() 

def travel(driver):
    driver.get("https://web.simple-mmo.com/travel")
    assert "Travel" in driver.title

def take_step(driver):
    element = driver.find_element(By.ID, "step_button")
    
    while True:
        element.click()
        time.sleep(10)

if __name__ == "__main__":
    main()