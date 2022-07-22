from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#paths
chrome_driver_path = r"C:\Users\Dell\Development\chromedriver_win32\chromedriver"
url =  "http://orteil.dashnet.org/experiments/cookie/"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url=url)

#cookie
cookie = driver.find_element(By.ID,'cookie')

#store items
store_items = driver.find_elements(By.CSS_SELECTOR,"#store div")
item_ids = [item.get_attribute("id") for item in store_items]
#print(item_ids)

five_sec = time.time() + 5
five_min = time.time() + 60*5
test = 0
while True:
    cookie.click()
    if time.time() > five_sec:
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = []

        for price in all_prices:
            price_text = price.text
            if price_text != "":
                cost = int(price_text.split("-")[1].strip().replace(",",""))
                item_prices.append(cost)

        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        money_element = driver.find_element(By.ID,'money').text
        if ',' in money_element:
            money_element=money_element.replace(",","")
        cookie_count = int(money_element)

        affordable_upgrades = {}
        for cost,id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        highest_available_upgrade = max(affordable_upgrades)
        purchase_id = affordable_upgrades[highest_available_upgrade]

        driver.find_element(By.ID,purchase_id).click()

        five_sec = time.time()+5

    if time.time() > five_min:
        cookie_per_sec = driver.find_element(By.ID, 'cps').text
        print(cookie_per_sec)
        break


