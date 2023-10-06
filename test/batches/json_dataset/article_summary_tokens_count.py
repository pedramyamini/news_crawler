import json
import os
import sys
import matplotlib.pyplot as plt

#read json
path = "C:\\Users\\Pedram\\OneDrive\\Research\\Dr Daneshfar\\Crawler\\Rudaw\\test\\final_json_dataset\\final_stable"
print("path: ", path)
dataset_filename = input("Enter dataset_filename: ")
with open(os.path.join(path,dataset_filename),"r",encoding="utf-8") as f:
    if dataset_filename != "final_dataset_stable.json":
        instances = json.load(f)
        instances = instances["data"]
    else:
        instances = json.load(f)
    



# font_size = 13
# plt.rcParams.update({'font.size': font_size})
# plt.xticks(fontsize=font_size)
# plt.yticks(fontsize=font_size)


#histogram of tokens count in the articles
tokens_count = [x["article_token_count"] for x in instances]
atc = tokens_count
#print("atc:",tokens_count)
#print("--------------------------------------------------------")
#fig, ax = plt.subplots()
#ax.hist(tokens_count, bins=100)
#ax.set_xlabel('Article tokens count')
#ax.set_ylabel('Frequency')
#ax.set_title('Article tokens count histogram')
#fig.savefig(os.path.join(os.getcwd(),"Rudaw","test","batches","json_dataset","article_token_count_histogram.png"),dpi=500)
#plt.show()

#histogram of tokens count in the summaries
tokens_count = [x["summary_token_count"] for x in instances]
stc = tokens_count
#print("stc",tokens_count)
#print("--------------------------------------------------------")
# fig, ax = plt.subplots()
# ax.hist(tokens_count, bins=100)
# ax.set_xlabel('Summary tokens count')
# ax.set_ylabel('Frequency')
# ax.set_title('Summary tokens count histogram')
# fig.savefig(os.path.join(os.getcwd(),"Rudaw","test","batches","json_dataset","summary_token_count_histogram.png"),dpi=500)
#plt.show()

#histogram of summary length
summary_length = [x["summary_length"] for x in instances]
sl = summary_length
#print("sl",summary_length)
#print("--------------------------------------------------------")
# fig, ax = plt.subplots()
# ax.hist(summary_length, bins=100)
# ax.set_xlabel('Summary length')
# ax.set_ylabel('Frequency')
# ax.set_title('Summary length histogram')
# fig.savefig(os.path.join(os.getcwd(),"Rudaw","test","batches","json_dataset","summary_length_histogram.png"),dpi=500)
#plt.show()

#histogram of article length
article_length = [x["article_length"] for x in instances]
al = article_length
#print("al",article_length)
#print("--------------------------------------------------------")
# print(article_length)
# fig, ax = plt.subplots()
# ax.hist(article_length, bins=100)
# ax.set_xlabel('Article length')
# ax.set_ylabel('Frequency')
# ax.set_title('Article length histogram')
# fig.savefig(os.path.join(os.getcwd(),"Rudaw","test","batches","json_dataset","article_length_histogram.png"),dpi=500)
#plt.show()

import csv

cols = ["atc","stc","al","sl"]
rows = []
for i in range(0,len(atc)):
    rows.append([atc[i], stc[i], al[i], sl[i]])

with open(os.path.join(path,dataset_filename.split('.')[0]+'_article_summary_token_count.csv'), 'w') as f:
    # using csv.writer method from CSV package
    write = csv.writer(f)

    write.writerow(cols)
    write.writerows(rows)
