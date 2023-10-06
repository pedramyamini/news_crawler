import json
import os
import matplotlib.pyplot as plt

#read json
path = "C:\\Users\\Pedram\\OneDrive\\Research\\Dr Daneshfar\\Crawler\\Rudaw\\test\\final_json_dataset"
with open(os.path.join(path,"final_dataset.json"),"r",encoding="utf-8") as f:
    instances = json.load(f)

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

categorical_train_instances = [business, iraq, world, iran, syria, turkey, kurdistan, health, sports, culture_style]


#distribution of categories in the corpus
categories_labels = ['business', 'iraq', 'world', 'iran', 'syria', 'turkey', 'kurdistan', 'health', 'sports','culture-style']
categories_count = [len(x) for x in categorical_train_instances]

plt.style.use('_mpl-gallery')

fig, ax = plt.subplots()

font_size = 13
plt.rcParams.update({'font.size': font_size})
plt.xticks(fontsize=font_size)
plt.yticks(fontsize=font_size)

#maximize plot
mng = plt.get_current_fig_manager()
mng.full_screen_toggle()

#maximize fig
fig.set_size_inches(15, 7)


ax.set_title("Distribution of categories in the corpus")
ax.set_xlabel("Categories",fontdict={"size":font_size})
ax.set_ylabel("Count",fontdict={"size":font_size})
plt.xticks()
ax.set_xticklabels(categories_labels)
ax.bar(categories_labels,categories_count,width=1,linewidth=0.8,edgecolor="white")

for i, v in enumerate(categories_count):
    ax.text(i, v, str(v), color='black', fontweight='bold',horizontalalignment='center')

plt.tight_layout(pad=0)

fig.savefig(os.path.join(path,"distribution_of_categories.png"),dpi=1500)

plt.show()

