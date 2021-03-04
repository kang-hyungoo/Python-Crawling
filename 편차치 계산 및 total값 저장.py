import json
import os
import math
from pathlib import Path

def id_to_champ_name(champ_id):     
    if int(champ_id) == 86:

        ChampionName = '가렌'

    if int(champ_id) == 3:

        ChampionName = '갈리오'

    if int(champ_id) == 41:

        ChampionName = '갱플랭크'

    if int(champ_id) == 79:

        ChampionName = '그라가스'

    if int(champ_id) == 104:

        ChampionName = '그레이브즈'

    if int(champ_id) == 150:

        ChampionName = '나르'

    if int(champ_id) == 267:

        ChampionName = '나미'

    if int(champ_id) == 75:

        ChampionName = '나서스'

    if int(champ_id) == 111:

        ChampionName = '노틸러스'

    if int(champ_id) == 56:

        ChampionName = '녹턴'

    if int(champ_id) == 20:

        ChampionName = '누누'

    if int(champ_id) == 76:

        ChampionName = '니달리'

    if int(champ_id) == 518:

        ChampionName = '니코'

    if int(champ_id) == 122:

        ChampionName = '다리우스'

    if int(champ_id) == 131:

        ChampionName = '다이애나'

    if int(champ_id) == 119:

        ChampionName = '드레이븐'

    if int(champ_id) == 13:

        ChampionName = '라이즈'

    if int(champ_id) == 497:

        ChampionName = '라칸'

    if int(champ_id) == 33:

        ChampionName = '람머스'

    if int(champ_id) == 99:

        ChampionName = '럭스'

    if int(champ_id) == 68:

        ChampionName = '럼블'

    if int(champ_id) == 58:

        ChampionName = '레넥톤'

    if int(champ_id) == 89:

        ChampionName = '레오나'

    if int(champ_id) == 421:

        ChampionName = '렉사이'

    if int(champ_id) == 107:

        ChampionName = '렝가'

    if int(champ_id) == 236:

        ChampionName = '루시안'

    if int(champ_id) == 117:

        ChampionName = '룰루'

    if int(champ_id) == 7:

        ChampionName = '르블랑'

    if int(champ_id) == 64:

        ChampionName = '리 신'

    if int(champ_id) == 92:

        ChampionName = '리븐'

    if int(champ_id) == 127:

        ChampionName = '리산드라'

    if int(champ_id) == 11:

        ChampionName = '마스터 이'

    if int(champ_id) == 57:

        ChampionName = '마오카이'

    if int(champ_id) == 90:

        ChampionName = '말자하'

    if int(champ_id) == 54:

        ChampionName = '말파이트'

    if int(champ_id) == 82:

        ChampionName = '모데카이저'

    if int(champ_id) == 25:

        ChampionName = '모르가나'

    if int(champ_id) == 36:

        ChampionName = '문도 박사'

    if int(champ_id) == 21:

        ChampionName = '미스 포츈'

    if int(champ_id) == 432:

        ChampionName = '바드'

    if int(champ_id) == 110:

        ChampionName = '바루스'

    if int(champ_id) == 254:

        ChampionName = '바이'

    if int(champ_id) == 45:

        ChampionName = '베이가'

    if int(champ_id) == 67:

        ChampionName = '베인'

    if int(champ_id) == 161:

        ChampionName = '벨코즈'

    if int(champ_id) == 106:

        ChampionName = '볼리베어'

    if int(champ_id) == 201:

        ChampionName = '브라움'

    if int(champ_id) == 63:

        ChampionName = '브랜드'

    if int(champ_id) == 8:

        ChampionName = '블라디미르'

    if int(champ_id) == 53:

        ChampionName = '블리츠크랭크'

    if int(champ_id) == 112:

        ChampionName = '빅토르'

    if int(champ_id) == 78:

        ChampionName = '뽀삐'

    if int(champ_id) == 14:

        ChampionName = '사이온'

    if int(champ_id) == 517:

        ChampionName = '사일러스'

    if int(champ_id) == 35:

        ChampionName = '샤코'

    if int(champ_id) == 113:

        ChampionName = '세주아니'    

    if int(champ_id) == 37:

        ChampionName = '소나'

    if int(champ_id) == 16:

        ChampionName = '소라카'

    if int(champ_id) == 98:

        ChampionName = '쉔'

    if int(champ_id) == 102:

        ChampionName = '쉬바나'

    if int(champ_id) == 50:

        ChampionName = '스웨인'

    if int(champ_id) == 72:

        ChampionName = '스카너'

    if int(champ_id) == 15:

        ChampionName = '시비르'

    if int(champ_id) == 5:

        ChampionName = '신 짜오'

    if int(champ_id) == 134:

        ChampionName = '신드라'

    if int(champ_id) == 27:

        ChampionName = '신지드'

    if int(champ_id) == 412:

        ChampionName = '쓰레쉬'

    if int(champ_id) == 103:

        ChampionName = '아리'

    if int(champ_id) == 32:

        ChampionName = '아무무'

    if int(champ_id) == 136:

        ChampionName = '아우렐리온 솔'

    if int(champ_id) == 427:

        ChampionName = '아이번'

    if int(champ_id) == 268:

        ChampionName = '아지르'

    if int(champ_id) == 84:

        ChampionName = '아칼리'

    if int(champ_id) == 266:

        ChampionName = '아트록스'

    if int(champ_id) == 12:

        ChampionName = '알리스타'

    if int(champ_id) == 1:

        ChampionName = '애니'

    if int(champ_id) == 34:

        ChampionName = '애니비아'

    if int(champ_id) == 22:

        ChampionName = '애쉬'

    if int(champ_id) == 157:

        ChampionName = '야스오'

    if int(champ_id) == 245:

        ChampionName = '에코'

    if int(champ_id) == 60:

        ChampionName = '엘리스'

    if int(champ_id) == 62:

        ChampionName = '오공'

    if int(champ_id) == 516:

        ChampionName = '오른'

    if int(champ_id) == 61:

        ChampionName = '오리아나'

    if int(champ_id) == 2:

        ChampionName = '올라프'

    if int(champ_id) == 83:

        ChampionName = '요릭'

    if int(champ_id) == 77:

        ChampionName = '우디르'

    if int(champ_id) == 6:

        ChampionName = '우르곳'

    if int(champ_id) == 19:

        ChampionName = '워윅'

    if int(champ_id) == 350:

        ChampionName = '유미'

    if int(champ_id) == 39:

        ChampionName = '이렐리아'

    if int(champ_id) == 28:

        ChampionName = '이블린'

    if int(champ_id) == 81:

        ChampionName = '이즈리얼'

    if int(champ_id) == 420:

        ChampionName = '일라오이'

    if int(champ_id) == 59:

        ChampionName = '자르반 4세'

    if int(champ_id) == 498:

        ChampionName = '자야'

    if int(champ_id) == 143:

        ChampionName = '자이라'

    if int(champ_id) == 154:

        ChampionName = '자크'

    if int(champ_id) == 40:

        ChampionName = '잔나'

    if int(champ_id) == 24:

        ChampionName = '잭스'

    if int(champ_id) == 238:

        ChampionName = '제드'

    if int(champ_id) == 101:

        ChampionName = '제라스'

    if int(champ_id) == 126:

        ChampionName = '제이스'

    if int(champ_id) == 142:

        ChampionName = '조이'

    if int(champ_id) == 115:

        ChampionName = '직스'

    if int(champ_id) == 202:

        ChampionName = '진'

    if int(champ_id) == 26:

        ChampionName = '질리언'

    if int(champ_id) == 222:

        ChampionName = '징크스'

    if int(champ_id) == 31:

        ChampionName = '초가스'

    if int(champ_id) == 43:

        ChampionName = '카르마'

    if int(champ_id) == 164:

        ChampionName = '카밀'

    if int(champ_id) == 38:

        ChampionName = '카사딘'

    if int(champ_id) == 30:

        ChampionName = '카서스'

    if int(champ_id) == 69:

        ChampionName = '카시오페아'

    if int(champ_id) == 145:

        ChampionName = '카이사'

    if int(champ_id) == 121:

        ChampionName = '카직스'

    if int(champ_id) == 55:

        ChampionName = '카타리나'

    if int(champ_id) == 429:

        ChampionName = '칼리스타'

    if int(champ_id) == 85:

        ChampionName = '케넨'

    if int(champ_id) == 51:

        ChampionName = '케이틀린'

    if int(champ_id) == 141:

        ChampionName = '케인'

    if int(champ_id) == 10:

        ChampionName = '케일'

    if int(champ_id) == 96:

        ChampionName = '코그모'

    if int(champ_id) == 42:

        ChampionName = '코르키'

    if int(champ_id) == 133:

        ChampionName = '퀸'

    if int(champ_id) == 240:

        ChampionName = '클레드'

    if int(champ_id) == 246:

        ChampionName = '키아나'

    if int(champ_id) == 203:

        ChampionName = '킨드레드'

    if int(champ_id) == 44:

        ChampionName = '타릭'

    if int(champ_id) == 91:

        ChampionName = '탈론'

    if int(champ_id) == 163:

        ChampionName = '탈리야'

    if int(champ_id) == 223:

        ChampionName = '탐 켄치'

    if int(champ_id) == 48:

        ChampionName = '트런들'

    if int(champ_id) == 18:

        ChampionName = '트리스타나'

    if int(champ_id) == 23:

        ChampionName = '트린다미어'

    if int(champ_id) == 4:

        ChampionName = '트위스티드 페이트'

    if int(champ_id) == 29:

        ChampionName = '트위치'

    if int(champ_id) == 17:

        ChampionName = '티모'

    if int(champ_id) == 555:

        ChampionName = '파이크'

    if int(champ_id) == 80:

        ChampionName = '판테온'

    if int(champ_id) == 9:

        ChampionName = '피들스틱'

    if int(champ_id) == 114:

        ChampionName = '피오라'

    if int(champ_id) == 105:

        ChampionName = '피즈'

    if int(champ_id) == 74:

        ChampionName = '하이머딩거'

    if int(champ_id) == 120:

        ChampionName = '헤카림'

    return ChampionName

list_f = open("list.txt", 'w')
filenames = os.listdir(os.getcwd())
for filename in filenames:
    full_filename = os.path.join(filename)
    ext = os.path.splitext(full_filename)[-1]
    if ext == '.json': 
        save_filename = full_filename + '\n'
        list_f.write(save_filename)
        
list_f.close()

list_f = open("list.txt", 'r')

while True:
    list_line = list_f.readline()
    if not list_line: break     # list.txt에 저장된 목록이 더 이상 없으면 종료
        
    load_f = open(list_line[0:-1], 'r')
    
    file_champ_id = None
    
    if list_line[1] == '_':
        file_champ_id = list_line[0:1]
        
    if list_line[2] == '_':
        file_champ_id = list_line[0:2]
        
    if list_line[3] == '_':
        file_champ_id = list_line[0:3]
    
    file_data = dict()
    save_data = dict()
    save_data1 = dict()
    
    file_data = json.load(load_f)

    list_f1 = open("list.txt", 'r')

    max_temp = 0
    max_champ = None

    i = 0

    sum_pick = 0
    sum_win = 0

    while True:
        list_line = list_f1.readline()
        if not list_line: break     # list.txt에 저장된 목록이 더 이상 없으면 종료

        if list_line[1] == '_':
            champ_id = list_line[0:1]

        if list_line[2] == '_':
            champ_id = list_line[0:2]

        if list_line[3] == '_':
            champ_id = list_line[0:3]

        if int(file_champ_id) is not int(champ_id):
            pick_rate = file_data["data"][champ_id]["pick"]/file_data["data"][file_champ_id]["pick"]
            sum_pick = sum_pick + pick_rate
            if file_data["data"][champ_id]["pick"] is not 0:
                win_rate = file_data["data"][champ_id]["win"]/file_data["data"][champ_id]["pick"]
            else:
                win_rate = 0
            sum_win  = sum_win + win_rate    
            save_data1[i] = { "id" : 0, "pick rate" : 0 , "win rate" : 0 }
            save_data1[i]["id"] = champ_id
            save_data1[i]["pick rate"] = pick_rate
            save_data1[i]["win rate"] = win_rate

            i = i + 1
            
    list_f1.close()
    
    save_data["data"] = save_data1
    average_pick = sum_pick / (i - 1)
    average_win = sum_win / (i - 1)


    sum_pick = 0
    sum_win = 0
    sum_temp = 0;

    j = 0
    while j != i:
        pick_rate = save_data["data"][j]["pick rate"]
        win_rate = save_data["data"][j]["win rate"]
        champ_id = save_data["data"][j]["id"]
        if champ_id != int(file_champ_id):
            sum_temp = sum_temp + (pick_rate - average_pick) * (win_rate - average_win)
            sum_pick = sum_pick + pow((pick_rate - average_pick), 2)
            sum_win = sum_win + pow((win_rate - average_win), 2)

        j = j + 1

    pick_ax = math.sqrt(sum_pick / (j - 1))
    win_ax = math.sqrt(sum_win / (j - 1))

    standard_score = dict()
    standard_score = save_data1

    k = 0
    while k != i:
        standard_score[k]["pick rate"] = (10 * (save_data1[k]["pick rate"] - average_pick) / pick_ax) + 50
        standard_score[k]["win rate"] = (10 * (save_data1[k]["win rate"] - average_win) / win_ax) + 50
        champ_id = standard_score[k]["id"]
        
        ChampionName = id_to_champ_name(champ_id)
        standard_score[k]["champ name"] = ChampionName
        k = k + 1

    max_temp = 0
    max_champ = 0
    k = 0

    while k != i:
        standard_score[k]["total"] = standard_score[k]["pick rate"] * 0.4 + standard_score[k]["win rate"] * 0.6

        k = k + 1
    file_champ_name = id_to_champ_name(file_champ_id)
    
    path = Path(os.getcwd()+ "/save_standard_score")
    save_file_champ_name = id_to_champ_name(int(file_champ_id))
    if path.exists():
        file_name = str(path) + "/" + save_file_champ_name + ".json"
    else:
        path.mkdir()
        file_name = str(path) + save_file_champ_name + ".json"
    with open(file_name, 'w', encoding='utf-8') as make_file:
        json.dump(standard_score, make_file, indent="\t")
list_f.close()
