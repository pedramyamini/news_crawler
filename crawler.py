import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

print("Starting...")
driver = webdriver.Edge(executable_path = r"msedgedriver.exe")
driver.maximize_window()
driver.get("https://www.rudaw.net/")

try:
    categories_links = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.header__main-menu-link")))
    #each category
    for link in categories_links:
        driver.get(link.get_attribute("href"))
        #run a script to get all the article links of the category
        driver.execute_script("""
        
            function scrollToEnd() { window.scrollTo(0,document.body.scrollHeight) } i=1;newsCount=0; while(i<=100){newsCount=document.getElementsByClassName("article__link").length;
            scrollToEnd();await new Promise(done => setTimeout(() => done(), 10000));i++;if(newsCount == document.getElementsByClassName("article__link").length) { break; }}
        
        """)
        #sleep for a while to let the script run
        time.sleep(1000)
        links = driver.execute_script("return document.getElementsByClassName('article__link')")
        #each article
        for link in links:
            driver.get(link.get_attribute("href"))
            #sleep for a while to let the script run
            time.sleep(3)
            #get the article title
            title = driver.execute_script("return document.getElementsByClassName('article-main__title')[0].innerText")
            #get the article summary
            summary = driver.execute_script("""
                var strongs = document.querySelectorAll("strong");
                var summary='';
                for(i=0;i<strongs.length;i++){if(strongs[i].innerText.includes("رووداو")){summary = strongs[i+2].innerText;break;}}
                return summary;
            """)
            #get the article content
            content = driver.execute_script("""
                var selectionShareables = document.querySelectorAll(".selectionShareable");
                var content='';
                for(i=0;i<selectionShareables.length;i++){content += selectionShareables[i].innerText;}
            """)
            content = content.replace(summary, "")
            #write the article to a file
            category = link.get_attribute("innerText")
            with open(str(category)+"\\"+title+"_article.txt", "a") as f:
                f.write(content)
            with open(str(category)+"\\"+title+"_summary.txt", "a") as f:
                f.write(summary)
finally:
    driver.quit()