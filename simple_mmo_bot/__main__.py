import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.common.exceptions import NoSuchElementException
import requests
from requests.structures import CaseInsensitiveDict

URL = "https://web.simple-mmo.com/api/bot-verification"

HEADERS = CaseInsensitiveDict()

HEADERS["authority"] = "web.simple-mmo.com"
HEADERS["accept"] = "*/*"
HEADERS["accept-language"] = "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"
HEADERS["cache-control"] = "no-cache"
HEADERS["content-type"] = "application/json"

HEADERS["origin"] = "https://web.simple-mmo.com"
HEADERS["pragma"] = "no-cache"
HEADERS["referer"] = "https://web.simple-mmo.com/i-am-not-a-bot"
# HEADERS["sec-ch-ua"] = '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"'
# HEADERS["sec-ch-ua-mobile"] = "?0"
# HEADERS["sec-ch-ua-platform"] = "Windows"
HEADERS["sec-fetch-dest"] = "empty"
HEADERS["sec-fetch-mode"] = "cors"
HEADERS["sec-fetch-site"] = "same-origin"
HEADERS["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36"

HEADERS["cookies"] = "{remember}={remember_value}; {d_h}={d_h_value}; {xsrf}={xsrf_value}; {laravel}={laravel_value}"

BOT_VERIFICATION_BYPASS = {
    "clock": "$2y$10$BFgvOcXaoIvJlkOT1F2KVenCq5OLQYfberNmRb5z/VPfd4BEMeEDG",
    "pear": "$2y$10$Lvb95cWOiqhl9R.0CW.mSOCaghU9IUR.EJEr2LDQUwolD.b4soKbq",
    "hat": "$2y$10$ZO8eEYL0Hq0Np24.V171NOXo6MZXjU6zCrPs9tuG3iiN8DCfN0ulC",
    "rose": "$2y$10$AZoefdYkTmykVvfsLDW6c.Do15ev4OW6px30bGDofR8SA2lWmezcy",
    "pretzel": "$2y$10$6eOZNKg2ABVNzMh0LqHt1OamDCu6lbXYgi00NLW5FOEO2Jhc8RZSm",
    "lemon": "$2y$10$jFqV7G1AoSbrAeynx6jGy.ETZxRgYI/cCMpwUKDgbsHX5KCQe3uc2",
    "candy cane":"$2y$10$6kYReMTs4/.srD1V/W3kbuQihOXejOwi5rbP7BimrYUzGlUBlYWny"
}


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
    element.send_keys("")
    element = driver.find_element(By.NAME, "password")
    element.clear()
    element.send_keys("")
    element.send_keys(Keys.RETURN)


def get_driver():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(chrome_options=chrome_options)
    return driver
    # assert "No results found." not in driver.page_source
    # driver.close()


def travel(driver):
    driver.get("https://web.simple-mmo.com/travel")
    assert "Travel" in driver.title


def take_step(driver):
    assert "Travel" in driver.title

    while True:
        element = driver.find_element(By.ID, "step_button")
        element.click()
        time.sleep(10)
      # not_machine(driver)
        attack(driver)


def not_machine(driver):
    try:
        driver.find_element(By.LINK_TEXT, '"I\'m not a pesky machine"').click()
        main_window = driver.window_handles[0]
        bot_window = driver.window_handles[1]
        driver.switch_to.window(bot_window)
        assert "Player Verification" in driver.title
        element = driver.find_element(By.CSS_SELECTOR, ".text-2xl")
        item = element.text.lower()
        cookies = driver.get_cookies()
        remember = cookies[3]['name']
        remember_value = cookies[3]['value'] 
        d_h = cookies[1]['name']
        d_h_value = cookies[1]['value'] 
        xsrf = cookies[2]['name']
        xsrf_value = cookies[2]['value'] 
        laravel = cookies[0]['name']
        laravel_value = cookies[0]['value']
        HEADERS["cookies"] = HEADERS["cookies"].format(remember=remember, remember_value=remember_value,d_h=d_h, d_h_value=d_h_value,
        xsrf=xsrf, xsrf_value=xsrf_value, laravel=laravel, laravel_value=laravel_value) 

        # data = '{"data":"{image}","x":72,"y":376}'.format(image=BOT_VERIFICATION_BYPASS[item])
        data = {"data":BOT_VERIFICATION_BYPASS[item], "x":72, "y":376}

        resp = requests.post(URL, headers=HEADERS, data=json.dumps(data))
      
    except NoSuchElementException:
        return


def attack(driver):
    try:
        element = driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/main/div[2]/div/div[2]/div/div/div[4]/div/div/div[2]/div/span[2]/a[1]"
        )
        element.click()
        attack_mob(driver)
    except NoSuchElementException:
        return


def attack_mob(driver):
    assert "Attacking" in driver.title
    element = driver.find_element(By.ID, "attackButton")

    while True:

        try:
            time.sleep(5)
            driver.find_element(By.LINK_TEXT, "Close").click()
            break
        except NoSuchElementException:
            element.click()


if __name__ == "__main__":
    main()
