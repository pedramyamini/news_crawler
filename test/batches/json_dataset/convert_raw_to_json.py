import json
import os
import random
import matplotlib.pyplot as plt

#directories in the corpus folder
directories = os.walk(os.path.join(os.getcwd(),"test","batches","json_dataset","corpus"))

instances = []
json_dataset_train = {}
json_train_instances = []
json_dataset_test = {}
json_test_instances = []
json_dataset_validation = {}
json_validation_instances = []


for root,subdirs,files in directories:
    subdirs = [x for x in subdirs if "_" in x]
    for subdir in subdirs:
        category = subdir.split("_")[0]
        article = ''
        with open(os.path.join(root,subdir,'article.txt'),"r",encoding="utf-8") as f:
            article = f.read()
        summary = ''
        with open(os.path.join(root,subdir,'summary.txt'),"r",encoding="utf-8") as f:
            summary = f.read()
        link = ''
        with open(os.path.join(root,subdir,'link.txt'),"r",encoding="utf-8") as f:
            link = f.read().replace("\n","")
        summary_length = len(summary)
        article_length = len(article)
        summary_token_count = len(summary.split())
        article_token_count = len(article.split())

        instance = {
            "article": article,
            "summary": summary,
            "link": link,
            "category": category,
            "summary_length": summary_length,
            "article_length": article_length,
            "summary_token_count": summary_token_count,
            "article_token_count": article_token_count
        }

        instances.append(instance)

        #progress
        print(len(instances))
        

#save to json
with open(os.path.join(os.getcwd(),"test","batches","json_dataset","dataset.json"),"w",encoding="utf-8") as f:
    json.dump(instances,f)






