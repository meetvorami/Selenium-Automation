import random
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from useragent import user_agent

option = Options()

# not to open chrome
# option.add_argument("--headless=new")

# uncommnet if you want to keep browser open
# option.add_experimental_option("detach", True)

# add user agent
random_value = random.randint(0, len(user_agent) - 1)


user_agent = "user-agent=" + user_agent[random_value]
option.add_argument(user_agent)


# creating a driver object
driver = webdriver.Chrome(options=option)
driver.maximize_window()

url = "https://www.flipkart.com/search?q=smart+phones&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_1_1_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_1_1_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=smart+phones&requestId=77e247e7-713d-4e89-aca5-80f1bc5747cb&as-searchtext=s"
driver.get(url=url)
time.sleep(5)

mobile_block = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/div[2]")

all_mobiles = mobile_block.find_elements(By.CSS_SELECTOR, ".cPHDOP.col-12-12")

for data in all_mobiles:
    try:
        mobile_name = data.find_element(By.CLASS_NAME, "KzDlHZ").text
    except Exception:
        mobile_name = None

    try:
        discount_price = data.find_element(By.CSS_SELECTOR, ".Nx9bqj._4b5DiR").text
    except Exception:
        discount_price = None

    try:
        actual_price = data.find_element(By.CSS_SELECTOR, ".yRaY8j.ZYYwLA").text
    except Exception:
        actual_price = ""
    if mobile_name and discount_price:
        print("===================================")
        print("Mobile Name: ", mobile_name)
        print("discount price: ", discount_price)
        print("actual price: ", actual_price)
        print("===================================")
i = 0
while i < 5:
    try:
        next_button = data.find_element(
            By.XPATH,
            "/html/body/div/div/div[3]/div[1]/div[2]/div[26]/div/div/nav/a[11]",
        )
        next_button.click()

        time.sleep(5)
    except Exception:
        break
    mobile_block = driver.find_element(
        By.XPATH, "/html/body/div/div/div[3]/div[1]/div[2]"
    )

    all_mobiles = mobile_block.find_elements(By.CSS_SELECTOR, ".cPHDOP.col-12-12")

    for data in all_mobiles:
        try:
            mobile_name = data.find_element(By.CLASS_NAME, "KzDlHZ").text
        except Exception:
            mobile_name = None

        try:
            discount_price = data.find_element(By.CSS_SELECTOR, ".Nx9bqj._4b5DiR").text
        except Exception:
            discount_price = None
        try:
            actual_price = data.find_element(By.CSS_SELECTOR, ".yRaY8j.ZYYwLA").text
        except Exception:
            actual_price = ""
        if mobile_name and discount_price:
            print("===================================")
            print("Mobile Name: ", mobile_name)
            print("discount price: ", discount_price)
            print("actual price: ", actual_price)
            print("===================================")
