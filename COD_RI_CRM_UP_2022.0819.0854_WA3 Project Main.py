import csv

class Cha:
    def __init__(self, att):
        for a, b in att.items():
            a = a.replace(" ", "_")
            a = a.replace("%", "p")
            self.__setattr__(a, b)

charas = {}

with open("COD_RI_CRM_UP_2022.0819.2128_WA3 Project CSV Character Dataset.csv") as charas_file:
    reader = csv.DictReader(charas_file)
    for row in reader:
        temp_dic = {}
        chara_name = ""
        for key, value in row.items():
            if key == "Name":  # get the name of the character
                chara_name = value
            else:
                try:
                    # try to convert value to float
                    temp_dic[key] = float(value)
                except:
                    # if failed, perhaps leave it alone as string
                    temp_dic[key] = value
        print(row, temp_dic)
        # create a new Character object using the Character class
        char = Cha(temp_dic)
        # inserting a dictionary item using character name
        charas[chara_name] = char

print(charas)

class Wea:
    def __init__(self, att):
        for a, b in att.items():
            a = a.replace(" ", "_")
            a = a.replace("%", "p")
            self.__setattr__(a, b)

weapons = {}

with open("COD_RI_CRM_UP_2022.0819.2128_WA3 Project Weapon CSV Dataset.csv") as weapons_file:
    reader = csv.DictReader(weapons_file)
    for row in reader:
        temp_dic = {}
        weap_name = ""
        for key, value in row.items():
            if key == "Name":  # get the name of the weapon
                weap_name = value
            else:
                try:
                    temp_dic[key] = float(value)
                except:
                    temp_dic[key] = value
        print(row, temp_dic)
        # create a new Weapon object using the Weapon class
        weap = Wea(temp_dic)
        # inserting a dictionary item using weapon name
        weapons[weap_name] = weap

print(weapons)

###

print('Welcome to the game assistent system, lets begin!')
chara_list = ['Traveler', 'Keqing', 'Mona', 'Jean', 'Diluc', 'Qiqi', 'Venti', 'Klee', 'Tartaglia', 'Zhongli', 'Albedo', 'Ganyu', 'Xiao', 'Hu Tao', 'Eula', 'Kaedehara Kazuha', 'Kamisato Ayaka', 'Yoimiya', 'Raiden Shogun', 'Aloy', 'Sangonomia Kokomi', 'Arakati Itto', 'Shenhe', 'Yae Miko', 'Kamisato Ayato', 'Yelan']
print("Let's start by choosing Character 1 in you team setup!")
for i in chara_list:
    print(f"\t [{chara_list.index(i) + 1}] {i}")
Char1 = int(input())
Char1 = chara_list[Char1 - 1]

class Art:
    def __init__(self, att):
        for a, b in att.items():
            a = a.replace(" ", "_")
            a = a.replace("%", "p")
            self.__setattr__(a, b)

qns = ["HP", "ATK","DEF","Elemental Mastery","CRIT Rate","CRIT DMG","Healing Bonus","Energy Recharge","Elemental DMG Bonus","Physical DMG Bonus"]

artifacts1 = {}
for qn in qns:
    artifacts[qn] = input(f"Enter your artifacts {qn} stat for {Char1}")
    artif = Art(artifacts1)
    artifacts1[Char1] = artif

artifacts2 = {}
for qn in qns:
    artifacts[qn] = input(f"Enter your artifacts {qn} stat for {Char2}")
    artif = Art(artifacts2)
    artifacts2[Char2] = artif

artifacts3 = {}
for qn in qns:
    artifacts[qn] = input(f"Enter your artifacts {qn} stat for {Char3}")
    artif = Art(artifacts3)
    artifacts3[Char3] = artif
    
artifacts4 = {}
for qn in qns:
    artifacts[qn] = input(f"Enter your artifacts {qn} stat for {Char4}")
    artif = Art(artifacts4)
    artifacts4[Char4] = artif
    



# # FIlter the weapon type
# print("""
# [1] Weapon Name
# [2] Weapon Name  """)
# wea1 = input('Enter the weapon for your first character')
# # retrive info on the character
# # c1_bhp =
# # c1_batk +=
# # c1_bdef =
# # c1_em =
# # c1_cr =
# # c1_cd =
# # c1_heal =
# # c1_er =
# # c1_eledb =
# # c1_phydb =
# # c1_atkp =
