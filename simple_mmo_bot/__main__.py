from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.common.exceptions import NoSuchElementException

BOT_VERIFICATION_BYPASS={"clock": "$2y$10$BFgvOcXaoIvJlkOT1F2KVenCq5OLQYfberNmRb5z/VPfd4BEMeEDG"}

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
    assert "Travel" in driver.title
    element = driver.find_element(By.ID, "step_button")
    
    while True:
        element.click()
        time.sleep(10)
        attack(driver)

def attack(driver):
    try: 
       element = driver.find_element_by_xpath("/html/body/div[1]/div[3]/main/div[2]/div/div[2]/div/div/div[4]/div/div/div[2]/div/span[2]/a[1]")
       element.click()
       attack_mob(driver)
    except NoSuchElementException:
        return

def attack_mob(driver):
    assert "Attacking" in driver.title
    element = driver.find_element(By.ID, "attackButton")
    
    while True:

        try:
            time.sleep(3)
            button = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[1]/div[3]/a[contains(., 'Close')]")
            button.click()
            break
        except NoSuchElementException:
            element.click()
            time.sleep(5)

            
        
if __name__ == "__main__":
    main()