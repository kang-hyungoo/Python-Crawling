import json
import os
import math
from pathlib import Path
import matplotlib.pyplot as plt

champ_name = input("확인하고 싶은 챔프를 입력해주세요 : ")
path = Path(os.getcwd()+ "/save_standard_score/" + champ_name + ".json")

if os.path.isfile:
    print("선택된 챔프가 있습니다.")
    load_f = open(path, 'r')
    
    file_data = dict()
    file_data = json.load(load_f)
    
    save_data = dict()
    
    count = len(file_data)
    
    print(file_data[str(0)])
    i = 0
    j = 0
    while i < count:
        if file_data[str(i)]["pick rate"] >= 45:
            if file_data[str(i)]["win rate"] > 50:
                save_data[j] = { "champ name" : None, "pick rate" : 0 , "win rate" : 0, "total" : 0 }
                save_data[j]["champ name"] = file_data[str(i)]["champ name"]
                save_data[j]["pick rate"] = file_data[str(i)]["pick rate"]
                save_data[j]["win rate"] = file_data[str(i)]["win rate"]
                save_data[j]["total"] = file_data[str(i)]["total"]
                j = j + 1
        i = i + 1
    entries = sorted(save_data.items(), key=lambda items: items[1]['total'])
    data_set = json.dumps(entries, indent=4, ensure_ascii=False)
    i = 0
    champ_name = []
    total = []
    while i < j:
        champ_name.append(data_set[i]["champ name"])
        total.append(data_set[i]["total"])
        i = i + 1
        
    n_groups = len(champ_name)
    index = np.arange(n_groups)

    plt.bar(index, total, tick_label=champ_name, align='center')

    plt.xlabel('month')
    plt.ylabel('average rainfall (mm)')
    plt.title('Weather Bar Chart')
    plt.xlim( -1, n_groups)
    plt.ylim( 0, 400)
    plt.show()
    
else:
    print("선택된 챔프가 없습니다.")
