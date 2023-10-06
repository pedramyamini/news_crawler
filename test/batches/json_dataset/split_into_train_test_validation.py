from ctypes import sizeof
import json
import random
import os
import matplotlib.pyplot as plt


#read json file
path = "C:\\Users\\Pedram\\OneDrive\\Research\\Dr Daneshfar\\Crawler\\Rudaw\\test\\final_json_dataset"
with open(os.path.join(path,"final_json_dataset.json"),"r",encoding="utf-8") as f:
    instances = json.load(f)


#same distribution
business = [x for x in instances if x["category"] == "business"]
iraq = [x for x in instances if x["category"] == "iraq"]
world = [x for x in instances if x["category"] == "world"]
iran = [x for x in instances if x["category"] == "iran"]
syria = [x for x in instances if x["category"] == "syria"]
turkey = [x for x in instances if x["category"] == "turkey"]
kurdistan = [x for x in instances if x["category"] == "kurdistan"]
#middleeast = [x for x in instances if x["category"] == "middleeast"]
health = [x for x in instances if x["category"] == "health"]
sports = [x for x in instances if x["category"] == "sports"]
#culture = [x for x in instances if x["category"] == "culture"]
culture_style = [x for x in instances if x["category"] == "culture-style"]

categories = [business, iraq, world, iran, syria, turkey, kurdistan, health, sports, culture_style]
categories_names = ["business", "iraq", "world", "iran", "syria", "turkey", "kurdistan", "health", "sports", "culture-style"]

#split into train, test, validation with same category distribution
train_instances = []
test_instances = []
validation_instances = []
for cat in categories:
    random.shuffle(cat)
    cat_len = len(cat) - (len(cat)%10)
    print('category',cat[0]["category"],'init_len',len(cat),'final_len',cat_len)
    train_instances.extend(cat[:int(cat_len*0.9)])
    test_instances.extend(cat[int(cat_len*0.9):int(cat_len*0.95)])
    validation_instances.extend(cat[int(cat_len*0.95):])

#check length
print('initial',len(instances),'final',len(train_instances)+len(test_instances)+len(validation_instances))
print('train',len(train_instances),'percentage',len(train_instances)/len(instances)*100)
print('test',len(test_instances),'percentage',len(test_instances)/len(instances)*100)
print('validation',len(validation_instances),'percentage',len(validation_instances)/len(instances)*100)


#check each split distribution
splits = [train_instances, test_instances, validation_instances]
splits_names = ["train", "test", "validation"]
for split in splits:
    index = splits.index(split)
    split_name = splits_names[index]

    #split into categories
    business = [x for x in split if x["category"] == "business"]
    iraq = [x for x in split if x["category"] == "iraq"]
    world = [x for x in split if x["category"] == "world"]
    iran = [x for x in split if x["category"] == "iran"]
    syria = [x for x in split if x["category"] == "syria"]
    turkey = [x for x in split if x["category"] == "turkey"]
    kurdistan = [x for x in split if x["category"] == "kurdistan"]
    #middleeast = [x for x in split if x["category"] == "middleeast"]
    health = [x for x in split if x["category"] == "health"]
    sports = [x for x in split if x["category"] == "sports"]
    #culture = [x for x in split if x["category"] == "culture"]
    culture_style = [x for x in split if x["category"] == "culture-style"]
    split_categories = [business, iraq, world, iran, syria, turkey, kurdistan, health, sports, culture_style]
    split_categories_len = [len(x) for x in split_categories]

    fig, ax = plt.subplots()

    #maximize plot
    mng = plt.get_current_fig_manager()
    mng.full_screen_toggle()

    #maximize fig
    fig.set_size_inches(18.5, 10.5)

    ax.set_title(split_name+' distribution')
    ax.set_xlabel("Categories")
    ax.set_ylabel("Count")
    ax.set_xticklabels(categories_names)
    ax.bar(categories_names,split_categories_len)

    for i, v in enumerate(split_categories_len):
        ax.text(i, v, str(v), color='blue', fontweight='bold')

    fig.savefig(os.path.join(path,split_name+".png"))

    plt.show()


json_train = {}
json_test = {}
json_validation = {}
json_train['data'] = train_instances
json_test['data'] = test_instances
json_validation['data'] = validation_instances

#write to json file
with open(os.path.join(path,"train.json"),"w",encoding="utf-8") as f:
    json.dump(json_train,f,ensure_ascii=False)
with open(os.path.join(path,"test.json"),"w",encoding="utf-8") as f:
    json.dump(json_test,f,ensure_ascii=False)
with open(os.path.join(path,"validation.json"),"w",encoding="utf-8") as f:
    json.dump(json_validation,f,ensure_ascii=False)