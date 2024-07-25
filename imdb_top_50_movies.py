import random
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from useragent import user_agent

option = Options()

# not to open chrome
# option.add_argument("--headless=new")


# option.add_experimental_option("detach", True)

# add user agent
random_value = random.randint(0, len(user_agent) - 1)


# user_agent = "user-agent=" + user_agent[random_value]
# option.add_argument(user_agent)


# creating a driver object
driver = webdriver.Chrome(options=option)
driver.maximize_window()

# url = "https://www.imdb.com/list/ls055386972/"
url ="https://www.imdb.com/list/ls053181721/"

driver.get(url=url)
time.sleep(5)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(3)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

movie_list = driver.find_elements(By.CSS_SELECTOR,".ipc-metadata-list-summary-item")


for movie in movie_list:
    try:
        movie_name = movie.find_element(By.CSS_SELECTOR, ".ipc-title__text").text
        movie_name = movie_name.split(".",1)
        movie_name = movie_name[1]
    except Exception as e:
        movie_name = None
    try:
        directors = movie.find_elements(By.CSS_SELECTOR,".ipc-link.ipc-link--base.dli-director-item")
        director_name = ", ".join([actor.text for actor in directors])

    except Exception as e:
        directors = ""
    
    try:
        year = ""
        duration = ""
        year_and_duration = movie.find_elements(By.CSS_SELECTOR,".sc-b189961a-8.kLaxqf.dli-title-metadata-item")
        for index,value in enumerate(year_and_duration):
            if index == 0:
                year = value.text
            if index == 1:
                duration = value.text
    except Exception as e:
        print('e: ', e)
        year = ""
        duration = ""
    try:
        star = movie.find_element(By.CSS_SELECTOR,".ipc-rating-star--rating").text
    except Exception as e:
        star = ""
    
    try:
        voted_by = movie.find_element(By.CSS_SELECTOR,".ipc-rating-star--voteCount").text.strip()
    except Exception as e:
        voted_by = ""
    
    try:
        content = movie.find_element(By.CSS_SELECTOR,".ipc-html-content-inner-div").text
    except Exception as e:
        content = ""
    try:
        meta_score = movie.find_element(By.CSS_SELECTOR,".sc-b0901df4-0.bcQdDJ.metacritic-score-box").text
    except Exception as e:
        meta_score = ""
    try:
        actors = movie.find_elements(By.CSS_SELECTOR,".ipc-link.ipc-link--base.dli-cast-item")
        actors_name = ", ".join([actor.text for actor in actors])

    except Exception as e:
        print('e: ', e)
        actors_name = ""

    if movie_name:
        print("Movie name: ", movie_name)
        print("directors: ", director_name)
        print("year: ",year)
        print("duration: ",duration)
        print("Story: ", content)
        print("star: ",star)
        print("voted_by: ",voted_by)
        print("star cast: ",actors_name)
        print("meta score: ",meta_score)
        print("============================================")
 