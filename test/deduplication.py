import json
import os

#read json file
with open(os.path.join(os.getcwd(),"batches","json_dataset","dataset.json"),"r",encoding="utf-8") as f:
    instances = json.load(f)

#read all links
with open("article_links.txt","r",encoding="utf-8") as f:
    all_links = f.readlines()

crawled_links = [instance["link"] for instance in instances]

print(len(crawled_links))

ask = input("Enter y to continue: ")

remaining_links = []
if(ask == "y"):
    for link in all_links:
        link = link.replace("\n","")
        if link not in crawled_links:
            link += "\n"
            remaining_links.append(link)

    with open("remaining_links.txt","w+",encoding="utf-8") as f:
        f.writelines(remaining_links)