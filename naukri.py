import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
option = Options()

# not to open chrome
# option.add_argument("--headless=new")
# option.add_experimental_option("detach", True)


# creating a driver object
driver = webdriver.Chrome(options=option)
driver.maximize_window()


url ="https://www.naukri.com/companies-hiring-in-india?src=gnbCompanies_homepage_srch&title=MNCs%20actively%20hiring&categoryId=101&pageNo=1&qccompanyIndustry=109&qcallJobLocation=51"
driver.get(url)
time.sleep(5)

all_company_name = driver.find_elements(By.CSS_SELECTOR,".freeTuple")

for boxes in all_company_name:
    company_dict = {}
    try:
        c_name = boxes.find_element(By.CSS_SELECTOR,".main-4.ellipsis.title.typ-18Bold").text
        company_dict["Company Name"] = c_name
        
    except Exception as e:
        c_name = None
        continue
        
    try:
        company_link = boxes.find_element(By.CSS_SELECTOR,".titleAnchor")
        company_link = company_link.get_attribute("href")
    except Exception as e:
        continue

    company_link = company_link.replace("tab=jobs&","")
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(company_link)
    time.sleep(10)

    try:
        about_us = driver.find_element(By.CSS_SELECTOR,".about-us")
        about_us_text = about_us.find_element(By.CSS_SELECTOR,".read-more-text.description.typ-14Medium").text
        company_dict["About Us"] = about_us_text
    except Exception as e:
        pass

    try:
        more_info = driver.find_element(By.CSS_SELECTOR,".more-info")
        company_details = more_info.find_elements(By.CSS_SELECTOR,".info-item")
        for details in company_details:
            text = details.text.split(":",1)
            if len(text) > 1 :
                company_dict[text[0]] = text[1]
    except Exception as e:
        pass
    
    if c_name:
        for key,values in company_dict.items():
            print(key,": ",values)
        print("=========================================")
    driver.close()
    driver.switch_to.window(driver.window_handles[0]) 
