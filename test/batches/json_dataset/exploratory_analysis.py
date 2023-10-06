import json
import os


#read json file
with open(os.path.join(os.getcwd(),"dataset.json"),"r",encoding="utf-8") as f:
    instances = json.load(f)

#eploratory analysis
article_length = [al['article_length'] for al in instances]
print('max al',max(article_length))
print('min al',min(article_length))

article_token_count = [atc['article_token_count'] for atc in instances]
print('max atc',max(article_token_count))
print('mean atc',sum(article_token_count)/len(article_token_count))
article_token_count_mode = [atc['article_token_count'] for atc in instances]
print('mode atc',max(article_token_count_mode, key=article_token_count_mode.count))
print('median atc',sorted(article_token_count)[len(article_token_count)//2])
print('min atc',min(article_token_count))

summary_length = [sl['summary_length'] for sl in instances]
print('max sl',max(summary_length))
print('min sl',min(summary_length))

summary_token_count = [stc['summary_token_count'] for stc in instances]
print('max stc',max(summary_token_count))
print('mean stc',sum(summary_token_count)/len(summary_token_count))
summary_token_count_mode = [stc['summary_token_count'] for stc in instances]
print('mode stc',max(summary_token_count_mode, key=summary_token_count_mode.count))
print('median stc',sorted(summary_token_count)[len(summary_token_count)//2])
print('min stc',min(summary_token_count))

atc_gt_1024 = [x for x in instances if x["article_token_count"] > 1024]
print('atc_gt_1024',len(atc_gt_1024))
stc_gt_1024 = [x for x in instances if x["summary_token_count"] > 1024]
print('stc_gt_1024',len(stc_gt_1024))

atc_gt_512 = [x for x in instances if x["article_token_count"] > 512]
print('atc_gt_512',len(atc_gt_512))
stc_gt_512 = [x for x in instances if x["summary_token_count"] > 512]
print('stc_gt_512',len(stc_gt_512))

atc_gt_256 = [x for x in instances if x["article_token_count"] > 256]
print('atc_gt_256',len(atc_gt_256))
stc_gt_256 = [x for x in instances if x["summary_token_count"] > 256]
print('stc_gt_256',len(stc_gt_256))

atc_gt_128 = [x for x in instances if x["article_token_count"] > 128]
print('atc_gt_128',len(atc_gt_128))
stc_gt_128 = [x for x in instances if x["summary_token_count"] > 128]
print('stc_gt_128',len(stc_gt_128))



exit()

#split into train, test, validation
random.shuffle(instances)
train_instances = instances[:int(len(instances)*0.9)]
test_instances = instances[int(len(instances)*0.9):int(len(instances)*0.95)]
validation_instances = instances[int(len(instances)*0.95):]



#split into train, test, validation
for category in categorical_train_instances:
    category_size = len(category) - (len(category)%100)

    if(category_size == 0):
        continue
    print(category_size,"\n")

    category_train = category[:int(category_size*0.9)]
    category_test = category[int(category_size*0.9):int(category_size*0.95)]
    category_validation = category[int(category_size*0.95):]
    
    json_train_instances.extend(category_train)
    json_test_instances.extend(category_test)
    json_validation_instances.extend(category_validation)

json_dataset_train["data"] = json_train_instances
json_dataset_test["data"] = json_test_instances
json_dataset_validation["data"] = json_validation_instances
print("train: ",len(json_dataset_train))
print("test: ",len(json_dataset_test))
print("validation: ",len(json_dataset_validation))

with open(os.path.join(os.getcwd(),"test","batches","json_dataset","rudaw_dataset_train.json"),"w",encoding="utf-8") as f:
    json.dump(json_dataset_train,f,ensure_ascii=False)
with open(os.path.join(os.getcwd(),"test","batches","json_dataset","rudaw_dataset_test.json"),"w",encoding="utf-8") as f:
    json.dump(json_dataset_test,f,ensure_ascii=False)
with open(os.path.join(os.getcwd(),"test","batches","json_dataset","rudaw_dataset_validation.json"),"w",encoding="utf-8") as f:
    json.dump(json_dataset_validation,f,ensure_ascii=False)