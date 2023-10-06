import os
import re
import sys
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
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)
driver = Edge(options = options)
# driver = webdriver.Edge(executable_path = r"msedgedriver.exe")
driver.maximize_window()


with open('remaining_links.txt', 'r') as f:
    links = f.readlines()

records = []
for link in links:
    driver.get(link)
    time.sleep(10)
    paragraphs = driver.execute_script("return document.querySelectorAll('div.bodyContentMainParent.selectionShareable > div.selectionShareable');")
    content = [paragraph for paragraph in paragraphs if len(paragraph.get_attribute('innerText')) > 25]
    summary = content[0].get_attribute('innerText')
    article = ''
    for paragraph in content[1:]:
        article += paragraph.get_attribute('innerText') + '\n'
    records.append((summary, article, link))
    
os.makedirs('corpus', exist_ok = True)

for record in records: 
    summary, article, link = record
    dir = link.split('/')[-2] + '_' + link.split('/')[-1]
    dir = dir.replace('\n', '')
    dir = os.path.join('corpus', dir)
    os.makedirs(dir, exist_ok = True)
    with open(os.path.join(dir, 'summary.txt'), 'w+',encoding='utf-8') as f:
        f.write(summary)
    with open(os.path.join(dir, 'article.txt'), 'w+',encoding='utf-8') as f:
        f.write(article)
    with open(os.path.join(dir, 'link.txt'), 'w+',encoding='utf-8') as f:
        f.write(link)
    