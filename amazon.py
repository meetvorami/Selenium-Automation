import random
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from useragent import user_agent

option = Options()

# not to open chrome
option.add_argument("--headless=new")


# option.add_experimental_option("detach", True)

# add user agent
random_value = random.randint(0, len(user_agent) - 1)


# user_agent = "user-agent=" + user_agent[random_value]
# option.add_argument(user_agent)


# creating a driver object
driver = webdriver.Chrome(options=option)
driver.maximize_window()


url ="https://www.amazon.in/s?k=smartphones&crid=DEFWBXQ9J9QS&sprefix=smartphone%2Caps%2C195&ref=nb_sb_noss_1"
driver.get(url)

mobile_data = driver.find_elements(By.CSS_SELECTOR,".a-section")

for mobile in mobile_data:
    try:
        name = mobile.find_element(By.CSS_SELECTOR,".a-size-medium.a-color-base.a-text-normal").text
    except Exception as e:
        name = None
    
    try: 
        sales_price = mobile.find_element(By.CSS_SELECTOR,".a-price").text
    except Exception as e:
        sales_price = ""
    try:
        actual_price = mobile.find_element(By.CSS_SELECTOR,".a-price.a-text-price").text
    except Exception as e:
        actual_price = ""
    if name and sales_price:
        print("Mobile Name: ", name)
        print("Sales Price: ",sales_price)
        print("Actual Price: ", actual_price)
        print("================================================")



i = 0

while i < 5 :
    i +=1 
    print("\n\n")
    print("page: ",i+1)

    try:
        button = driver.find_element(By.CSS_SELECTOR,".s-pagination-item.s-pagination-next.s-pagination-button.s-pagination-separator")
    except Exception as e:
        break
    


    mobile_data = driver.find_elements(By.CSS_SELECTOR,".a-section")
    
    for mobile in mobile_data:
        try:
            name = mobile.find_element(By.CSS_SELECTOR,".a-size-medium.a-color-base.a-text-normal").text
        except Exception as e:
            name = None
        
        try: 
            sales_price = mobile.find_element(By.CSS_SELECTOR,".a-price").text
        except Exception as e:
            sales_price = ""
        try:
            actual_price = mobile.find_element(By.CSS_SELECTOR,".a-price.a-text-price").text
        except Exception as e:
            actual_price = ""
        if name and sales_price:
            print("Mobile Name: ", name)
            print("Sales Price: ",sales_price)
            print("Actual Price: ", actual_price)
            print("================================================")