import json
import os

#read json
path = "C:\\Users\\Pedram\\OneDrive\\Research\\Dr Daneshfar\\Crawler\\Rudaw\\test\\final_json_dataset\\final_stable"
with open(os.path.join(path,"train.json"),"r",encoding="utf-8") as f:
    train = json.load(f)
    train = train["data"]
with open(os.path.join(path,"test.json"),"r",encoding="utf-8") as f:
    test = json.load(f)
    test = test["data"]
with open(os.path.join(path,"validation.json"),"r",encoding="utf-8") as f:
    validation = json.load(f)
    validation = validation["data"]


final_dataset = train + test + validation

print(len(final_dataset))

answer = input("continue? (y/n): ")
if answer == "y":
    with open(os.path.join(path,"final_dataset_stable.json"),"w+",encoding="utf-8") as f:
        json.dump(final_dataset,f)
