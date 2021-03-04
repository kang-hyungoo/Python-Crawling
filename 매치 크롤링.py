import pandas as pd

import numpy as np

import os

import json

import requests

import time as t


api_key = 'RGAPI-43fae57f-e970-4d49-8b1e-59d46fa03b3a'

m = 0

while m < 100000:
    
    matchId = '3896756128'

    change = int(matchId) - m

    matchId = str(change)

    matchData = 'https://kr.api.riotgames.com/lol/match/v4/matches/'+ matchId + '?api_key=' + api_key

    r = requests.get(matchData)

    print("시작")

    print(r.status_code)

    if r.status_code == 200:

        content = json.loads(r.content)

        if str(content['teams'][0]['bans']) != '[]':

            if content['mapId'] == 11:
        
                team100_win = content['teams'][0]['win']

                team100_bans = content['teams'][0]['bans']

                team200_win = content['teams'][1]['win']

                team200_bans = content['teams'][1]['bans']

                if content['gameVersion'][4] == '.':

                    gameVersion = content['gameVersion'][0:4]

                else:

                    gameVersion = content['gameVersion'][0:5]

     

                print('확인중 : ' + matchId)

     

                i = 0

     

                while i < 10:
                    
                    leagueData = 'https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/' + str(content['participantIdentities'][i]['player']['summonerId']) + '?api_key=' + api_key

                    r1 = requests.get(leagueData)
                    
                    if r1.status_code == 200:
                        
                        content1 = json.loads(r1.content)
                        
                    else:
                        
                        while r1.status_code != 200:

                            leagueData = 'https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/' + str(content['participantIdentities'][i]['player']['summonerId']) + '?api_key=' + api_key

                            r1 = requests.get(leagueData)

                            content1 = json.loads(r1.content)

                            t.sleep(1)

                    print(i)
                    
                    j = 0 

                    while j < len(content1):
                        
                        if content1[j]['queueType'] == 'RANKED_SOLO_5x5':    
                            
                            ChampionName = None
                            
                            print(content1[j]['tier'])
                            
                            if content1[j]['tier'] == 'PLATINUM' or content1[j]['tier'] == 'DIAMOND' or content1[j]['tier'] == 'MASTER' or content1[j]['tier'] == 'GRANDMASTER' or content1[j]['tier'] == 'CHALLENGER':
                                
                                PickChampionName = id_to_champ_name(content['participants'][i]['championId'])
                            

                                print('픽 : ' + PickChampionName)

                                file_name = str(content['participants'][i]['championId']) + '_' + str(gameVersion) + '_' + '.json'

                                file_data1 = dict()

                                if os.path.isfile(file_name):

                                    print('파일 있음')

                                    with open(file_name, 'r') as f:

                                        file_data1 = json.load(f)

                                else:

                                    print('파일 없음')

                                    file_data = dict()

                                    file_data["86"] = {  "pick" : 0, "win" : 0 }

                                    file_data["3"] = {  "pick" : 0, "win" : 0 }

                                    file_data["41"] = {  "pick" : 0, "win" : 0 }

                                    file_data["79"] = {  "pick" : 0, "win" : 0 }

                                    file_data["104"] = {  "pick" : 0, "win" : 0 }

                                    file_data["150"] = {  "pick" : 0, "win" : 0 }

                                    file_data["267"] = {  "pick" : 0, "win" : 0 }

                                    file_data["75"] = {  "pick" : 0, "win" : 0 } 

                                    file_data["111"] = {  "pick" : 0, "win" : 0 }

                                    file_data["56"] = {  "pick" : 0, "win" : 0 }

                                    file_data["20"] = {  "pick" : 0, "win" : 0 }

                                    file_data["76"] = {  "pick" : 0, "win" : 0 }

                                    file_data["518"] = {  "pick" : 0, "win" : 0 }

                                    file_data["122"] = {  "pick" : 0, "win" : 0 }

                                    file_data["131"] = {  "pick" : 0, "win" : 0 }

                                    file_data["119"] = {  "pick" : 0, "win" : 0 }

                                    file_data["13"] = {  "pick" : 0, "win" : 0 }

                                    file_data["497"] = {  "pick" : 0, "win" : 0 }

                                    file_data["33"] = {  "pick" : 0, "win" : 0 }

                                    file_data["99"] = {  "pick" : 0, "win" : 0 }

                                    file_data["68"] = {  "pick" : 0, "win" : 0 }

                                    file_data["58"] = {  "pick" : 0, "win" : 0 }

                                    file_data["89"] = {  "pick" : 0, "win" : 0 }

                                    file_data["421"] = {  "pick" : 0, "win" : 0 }

                                    file_data["107"] = {  "pick" : 0, "win" : 0 }

                                    file_data["236"] = {  "pick" : 0, "win" : 0 }

                                    file_data["117"] = {  "pick" : 0, "win" : 0 }

                                    file_data["7"] = {  "pick" : 0, "win" : 0 }

                                    file_data["64"] = {  "pick" : 0, "win" : 0 }

                                    file_data["92"] = {  "pick" : 0, "win" : 0 }

                                    file_data["127"] = {  "pick" : 0, "win" : 0 }

                                    file_data["11"] = {  "pick" : 0, "win" : 0 }

                                    file_data["57"] = {  "pick" : 0, "win" : 0 }

                                    file_data["90"] = {  "pick" : 0, "win" : 0 }

                                    file_data["54"] = {  "pick" : 0, "win" : 0 }

                                    file_data["82"] = {  "pick" : 0, "win" : 0 }

                                    file_data["25"] = {  "pick" : 0, "win" : 0 }

                                    file_data["36"] = {  "pick" : 0, "win" : 0 }

                                    file_data["21"] = {  "pick" : 0, "win" : 0 }

                                    file_data["432"] = {  "pick" : 0, "win" : 0 }

                                    file_data["110"] = {  "pick" : 0, "win" : 0 }

                                    file_data["254"] = {  "pick" : 0, "win" : 0 }

                                    file_data["45"] = {  "pick" : 0, "win" : 0 }

                                    file_data["67"] = {  "pick" : 0, "win" : 0 }

                                    file_data["161"] = {  "pick" : 0, "win" : 0 }

                                    file_data["106"] = {  "pick" : 0, "win" : 0 }

                                    file_data["201"] = {  "pick" : 0, "win" : 0 }

                                    file_data["63"] = {  "pick" : 0, "win" : 0 }

                                    file_data["8"] = {  "pick" : 0, "win" : 0 }

                                    file_data["53"] = {  "pick" : 0, "win" : 0 }

                                    file_data["112"] = {  "pick" : 0, "win" : 0 }

                                    file_data["78"] = {  "pick" : 0, "win" : 0 }

                                    file_data["14"] = {  "pick" : 0, "win" : 0 }

                                    file_data["517"] = {  "pick" : 0, "win" : 0 }

                                    file_data["35"] = {  "pick" : 0, "win" : 0 }

                                    file_data["113"] = {  "pick" : 0, "win" : 0 }   

                                    file_data["37"] = {  "pick" : 0, "win" : 0 }

                                    file_data["16"] = {  "pick" : 0, "win" : 0 }

                                    file_data["98"] = {  "pick" : 0, "win" : 0 }

                                    file_data["102"] = {  "pick" : 0, "win" : 0 }

                                    file_data["50"] = {  "pick" : 0, "win" : 0 }

                                    file_data["72"] = {  "pick" : 0, "win" : 0 }

                                    file_data["15"] = {  "pick" : 0, "win" : 0 }

                                    file_data["5"] = {  "pick" : 0, "win" : 0 }

                                    file_data["134"] = {  "pick" : 0, "win" : 0 }

                                    file_data["27"] = {  "pick" : 0, "win" : 0 }

                                    file_data["412"] = {  "pick" : 0, "win" : 0 }

                                    file_data["103"] = {  "pick" : 0, "win" : 0 }

                                    file_data["32"] = {  "pick" : 0, "win" : 0 }

                                    file_data["136"] = {  "pick" : 0, "win" : 0 }

                                    file_data["427"] = {  "pick" : 0, "win" : 0 }

                                    file_data["268"] = {  "pick" : 0, "win" : 0 }

                                    file_data["84"] = {  "pick" : 0, "win" : 0 }

                                    file_data["266"] = {  "pick" : 0, "win" : 0 }

                                    file_data["12"] = {  "pick" : 0, "win" : 0 }

                                    file_data["1"] = {  "pick" : 0, "win" : 0 }

                                    file_data["34"] = {  "pick" : 0, "win" : 0 }

                                    file_data["22"] = {  "pick" : 0, "win" : 0 }

                                    file_data["157"] = {  "pick" : 0, "win" : 0 }

                                    file_data["245"] = {  "pick" : 0, "win" : 0 }

                                    file_data["60"] = {  "pick" : 0, "win" : 0 }

                                    file_data["62"] = {  "pick" : 0, "win" : 0 }

                                    file_data["516"] = {  "pick" : 0, "win" : 0 }

                                    file_data["61"] = {  "pick" : 0, "win" : 0 }

                                    file_data["2"] = {  "pick" : 0, "win" : 0 }

                                    file_data["83"] = {  "pick" : 0, "win" : 0 }

                                    file_data["77"] = {  "pick" : 0, "win" : 0 }

                                    file_data["6"] = {  "pick" : 0, "win" : 0 }

                                    file_data["19"] = {  "pick" : 0, "win" : 0 }

                                    file_data["350"] = {  "pick" : 0, "win" : 0 }

                                    file_data["39"] = {  "pick" : 0, "win" : 0 }

                                    file_data["28"] = {  "pick" : 0, "win" : 0 }

                                    file_data["81"] = {  "pick" : 0, "win" : 0 }

                                    file_data["420"] = {  "pick" : 0, "win" : 0 }

                                    file_data["59"] = {  "pick" : 0, "win" : 0 }

                                    file_data["498"] = {  "pick" : 0, "win" : 0 }

                                    file_data["143"] = {  "pick" : 0, "win" : 0 }

                                    file_data["154"] = {  "pick" : 0, "win" : 0 }

                                    file_data["40"] = {  "pick" : 0, "win" : 0 }

                                    file_data["24"] = {  "pick" : 0, "win" : 0 }

                                    file_data["238"] = {  "pick" : 0, "win" : 0 }

                                    file_data["101"] = {  "pick" : 0, "win" : 0 }

                                    file_data["126"] = {  "pick" : 0, "win" : 0 }

                                    file_data["142"] = {  "pick" : 0, "win" : 0 }

                                    file_data["115"] = {  "pick" : 0, "win" : 0 }

                                    file_data["202"] = {  "pick" : 0, "win" : 0 }

                                    file_data["26"] = {  "pick" : 0, "win" : 0 }

                                    file_data["222"] = {  "pick" : 0, "win" : 0 }

                                    file_data["31"] = {  "pick" : 0, "win" : 0 }

                                    file_data["43"] = {  "pick" : 0, "win" : 0 }

                                    file_data["164"] = {  "pick" : 0, "win" : 0 }

                                    file_data["38"] = {  "pick" : 0, "win" : 0 }

                                    file_data["30"] = {  "pick" : 0, "win" : 0 }

                                    file_data["69"] = {  "pick" : 0, "win" : 0 }

                                    file_data["145"] = {  "pick" : 0, "win" : 0 }

                                    file_data["121"] = {  "pick" : 0, "win" : 0 }

                                    file_data["55"] = {  "pick" : 0, "win" : 0 }

                                    file_data["429"] = {  "pick" : 0, "win" : 0 }

                                    file_data["85"] = {  "pick" : 0, "win" : 0 }

                                    file_data["51"] = {  "pick" : 0, "win" : 0 }

                                    file_data["141"] = {  "pick" : 0, "win" : 0 }

                                    file_data["10"] = {  "pick" : 0, "win" : 0 }

                                    file_data["96"] = {  "pick" : 0, "win" : 0 }

                                    file_data["42"] = {  "pick" : 0, "win" : 0 }

                                    file_data["133"] = {  "pick" : 0, "win" : 0 }

                                    file_data["240"] = {  "pick" : 0, "win" : 0 }

                                    file_data["246"] = {  "pick" : 0, "win" : 0 }

                                    file_data["203"] = {  "pick" : 0, "win" : 0 }

                                    file_data["44"] = {  "pick" : 0, "win" : 0 }

                                    file_data["91"] = {  "pick" : 0, "win" : 0 }

                                    file_data["163"] = {  "pick" : 0, "win" : 0 }

                                    file_data["223"] = {  "pick" : 0, "win" : 0 }

                                    file_data["48"] = {  "pick" : 0, "win" : 0 }

                                    file_data["18"] = {  "pick" : 0, "win" : 0 }

                                    file_data["23"] = {  "pick" : 0, "win" : 0 }

                                    file_data["4"] = {  "pick" : 0, "win" : 0 }

                                    file_data["29"] = {  "pick" : 0, "win" : 0 }

                                    file_data["17"] = {  "pick" : 0, "win" : 0 }

                                    file_data["555"] = {  "pick" : 0, "win" : 0 }

                                    file_data["80"] = {  "pick" : 0, "win" : 0 }

                                    file_data["9"] = {  "pick" : 0, "win" : 0 }

                                    file_data["114"] = {  "pick" : 0, "win" : 0 }

                                    file_data["105"] = {  "pick" : 0, "win" : 0 }

                                    file_data["74"] = {  "pick" : 0, "win" : 0 }

                                    file_data["120"] = {  "pick" : 0, "win" : 0 }

                                    file_data1["data"] = file_data

                                    with open(file_name, 'w', encoding='utf-8') as make_file:

                                         json.dump(file_data1, make_file, indent="\t")

                                if i < 5:

                                    y = 0

                                    while y < 5:

                                        champ_id_save = str(content['participants'][y]['championId'])

                                        file_data1["data"][champ_id_save]["pick"] = file_data1["data"][champ_id_save]["pick"] + 1

                                        if team100_win =='Win':

                                            file_data1["data"][champ_id_save]["win"] = file_data1["data"][champ_id_save]["win"] + 1

                                        y = y + 1

                                    with open(file_name, 'w', encoding='utf-8') as make_file:

                                        json.dump(file_data1, make_file, indent="\t")

                                    print(file_name)

                                else:

                                    y = 5

                                    while y < 10:

                                        champ_id_save = str(content['participants'][y]['championId'])

                                        file_data1["data"][champ_id_save]["pick"] = file_data1["data"][champ_id_save]["pick"] + 1

                                        if team200_win =='Win':

                                            file_data1["data"][champ_id_save]["win"] = file_data1["data"][champ_id_save]["win"] + 1

                                        y = y + 1

                                    with open(file_name, 'w', encoding='utf-8') as make_file:

                                        json.dump(file_data1, make_file, indent="\t")

                                    print(file_name)

                        j = j + 1
                        

                    t.sleep(1)

                    i = i + 1

                print('확인완료')

                t.sleep(4)
                
            else:
                
                print('오류 : ' + content['gameType'] + ' ' + matchId)
            
                t.sleep(14)
        else:
            
            print('오류 : no Rank ' + matchId)
            
            t.sleep(14)
 
    else:
        
        print('오류 : ' + matchId)
        
        t.sleep(14)

    m = m + 1


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
