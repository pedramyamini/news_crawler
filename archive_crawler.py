import os
import re
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from msedge.selenium_tools import Edge, EdgeOptions
import time

def save_file(file_path, content):
    URLs = ''
    for url in content:
        URLs += url + '\n'
    with open(file_path, 'a+') as f:
        f.write(URLs)

print("Starting...")
options = EdgeOptions()
options.use_chromium = True
options.add_argument('headless')
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)
driver = Edge(options = options)
# driver = webdriver.Edge(executable_path = r"msedgedriver.exe")
driver.maximize_window()

try:
    # categories_links = WebDriverWait(driver, 10).until(
    #     EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.header__main-menu-link")))
    visited_cats = {
        
    }
    
    categories_links = [
        "https://www.rudaw.net/sorani/search-results/archive?CategoryID=412602",
        "https://www.rudaw.net/sorani/search-results/archive?CategoryID=412608",
        "https://www.rudaw.net/sorani/search-results/archive?CategoryID=412614",
        "https://www.rudaw.net/sorani/search-results/archive?CategoryID=412616",
        "https://www.rudaw.net/sorani/search-results/archive?CategoryID=412617",
        "https://www.rudaw.net/sorani/search-results/archive?CategoryID=412625",
        "https://www.rudaw.net/sorani/search-results/archive?CategoryID=412626",
        "https://www.rudaw.net/sorani/search-results/archive?CategoryID=412627",
        "https://www.rudaw.net/sorani/search-results/archive?CategoryID=412628",
        "https://www.rudaw.net/sorani/search-results/archive?CategoryID=414583",
        "https://www.rudaw.net/sorani/search-results/archive?CategoryID=414584",
        "https://www.rudaw.net/sorani/search-results/archive?CategoryID=412631",
        "https://www.rudaw.net/sorani/search-results/archive?CategoryID=412632",
    ]

    
    #each category
    for cat_link in categories_links:
        cat = cat_link.split('?')[1].replace('CategoryID=','')
        print("Category: " + cat_link)
        driver.get(cat_link);
        #run a script to get all the article links of the category
        driver.set_script_timeout(30)
        number = re.compile(r'\d+(?:\.\d+)?')
        numbers = number.findall(driver.find_element(By.CSS_SELECTOR,"#spanResults").get_attribute("innerText"))
        count = int(numbers[0])
        print("Count: " + str(count))
        clicks = count//12
        print("Clicks: " + str(clicks))
        time.sleep(5)

        # URLs = []
        for i in range(count):
            driver.execute_script('var loadMore = document.querySelector("aLoadMore");if(loadMore!=null){loadMore.click()}')
            time.sleep(15)
            # if(i % 100 == 0 and i != 0):
            #     links = driver.execute_script("return document.getElementsByClassName('article__link')")
            #     for link in links:
            #         URLs.append(link.get_attribute("href"))
            #     save_file(cat + '.txt', URLs[i:])
            # WebDriverWait(driver, 240).until(EC.element_to_be_clickable((By.ID, "aLoadMore"))).click()
        
        
        links = driver.execute_script("return document.getElementsByClassName('article__link')")
        URLs = []
        for link in links:
            URLs.append(link.get_attribute("href"))

        #save the URLs to a file
        save_file(cat + '.txt', URLs)
finally:
    driver.quit()