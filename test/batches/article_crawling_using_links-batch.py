import os
import re
import sys
from turtle import screensize
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from msedge.selenium_tools import Edge, EdgeOptions
import time
from threading import Thread


print("Starting...")
options = EdgeOptions()
options.use_chromium = True
options.add_argument('headless')
options.page_load_strategy = 'eager'
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_argument('--disable_browser_side_navigation')
options.add_experimental_option("prefs", prefs)
driver = Edge(options = options)
# driver = webdriver.Edge(executable_path = r"msedgedriver.exe")
driver.maximize_window()


with open('article_links.txt', 'r') as f:
    links = f.readlines()

instances_count = len(links)
batch_size = 1000
print(instances_count%batch_size)
batch_count = int(instances_count / batch_size)
if((instances_count%batch_size) > 0):
    batch_count += 1
print("Batch count:", batch_count)
batch = int(input("Enter #batch:"))

os.makedirs('corpus', exist_ok = True)


failed_links = ''

if batch * 1000 > instances_count:
    links = links[(batch-1)*batch_size:]
else:
    links = links[(batch-1)*batch_size:(batch-1)*batch_size+batch_size-1]

for link in links:
    index = links.index(link)
    print('----------------------------------------------------')
    print("Processing link #", index+1, ":", link)
    try:
        dir = link.split('/')[-2] + '_' + link.split('/')[-1]
        dir = dir.replace('\n', '')
        dir = os.path.join('corpus',str(batch), dir)

        received_before = [False,False,False]
        if os.path.exists(dir):
            print(dir)
            i = 0
            for file in os.listdir(dir):
                if os.path.getsize(os.path.join(dir, file)) > 0:
                    received_before[i] = True
                    i += 1    

        if received_before == [True,True,True]:
            print("Already received before.")
            continue

        driver.get(link)
        print("Waiting for page to load...")
        #paragraphs = driver.execute_script("return document.querySelectorAll('div.bodyContentMainParent.selectionShareable > div.selectionShareable');")
        paragraphs = driver.find_elements(By.XPATH,"//div[@style='text-align: justify;']")
        content = [paragraph for paragraph in paragraphs if len(paragraph.get_attribute('innerText')) > 25]
        summary = content[0].get_attribute('innerText')
        article = ''
        for paragraph in content[1:]:
            article += paragraph.get_attribute('innerText') + '\n'

        if (article == '' 
                or len(summary) >= 0.8*len(article)
                or len(summary) <= 50
                or len(summary.split('\n')) > 1):
            failed_links += link + '\n'
            print("Not Appropriate.")
            continue


        os.makedirs(dir, exist_ok = True)

        with open(os.path.join(dir, 'summary.txt'), 'w+', encoding='utf-8') as f:
            f.write(summary)
        with open(os.path.join(dir, 'article.txt'), 'w+', encoding='utf-8') as f:
            f.write(article)
        with open(os.path.join(dir, 'link.txt'), 'w+', encoding='utf-8') as f:
            f.write(link)
        
        print("Successfully received.")
    except:
        failed_links += link + '\n'
        print("Failed.")
        continue

dir = os.path.join('corpus',str(batch))
os.makedirs(dir, exist_ok=True)
file_path = os.path.join('corpus', str(batch), 'failed_links.txt')
with open(file_path, 'w+', encoding='utf-8') as f:
    f.write(failed_links)

driver.quit()