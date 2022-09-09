import csv

class Cha:
    def __init__(self, att):
        for a, b in att.items():
            a = a.replace(" ", "_")
            a = a.replace("%", "p")
            self.__setattr__(a, b)


characters = {}

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
        # create a new Character object using the Character class
        char = Cha(temp_dic)
        # inserting a dictionary item using character name
        characters[chara_name] = char

#print(characters)

class Wea:
    def __init__(self, att):
        for a, b in att.items():
            a = a.replace(" ", "1")
            a = a.replace("%", "P")
            a = a.replace("Rarity", "Rarity1")
            self.__setattr__(a, b)

    

weapons = {}

with open("COD_RI_CRM_UP_2022.0819.2204_WA3 Project CSV Weapon Dataset.csv") as weapons_file:
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
        # create a new Weapon object using the Weapon class
        weap = Wea(temp_dic)
        # inserting a dictionary item using weapon name
        weapons[weap_name] = weap


class Art:
    def __init__(self, att):
        for a, b in att.items():
            a = a.replace(" ", "2")
            self.__setattr__(a, b)

qns = ["HP","ATK","DEF","Elemental Mastery","CRIT Rate","CRIT DMG","Healing Bonus","Energy Recharge","Elemental DMG Bonus","Physical DMG Bonus"]

Char_attr = ['ATKp', 'Base_ATK', 'Base_DEF', 'Base_HP', 'CRIT_DMG', 'CRIT_Rate', 'Elemental_DMG_Bonus', 'Elemental_Mastery', 'Energy_Recharge', 'Healing_Bonus', 'Physical_DMG_Bonus'] #0 - 10
Wea_attr = ['ATKP', 'Base1ATK', 'CRIT1DMG', 'CRIT1Rate', 'DEFP', 'Elemental1DMG1Bonus', 'Elemental1Mastery', 'Energy1Recharge', 'HPP', 'Healing1Bonus', 'Physical1DMG1Bonus']# 11- 21
Art_attr = ['ATK', 'CRIT2DMG', 'CRIT2Rate', 'DEF', 'Elemental2DMG2Bonus', 'Elemental2Mastery', 'Energy2Recharge', 'HP', 'Healing2Bonus', 'Physical2DMG2Bonus'] #22 - 31

class team:
    def __init__(self, a):
        self.BATK = int(a[1] + a[12])
        self.ATK = int((a[1] + a[12]) * (a[0]/100 + a[11]/100) + a[22])
        self.BHP = int(a[3])
        self.HP = int(a[3] * (a[19]/100) + a[29])
        self.BDEF = int(a[2])
        self.DEF = int(a[2] * (a[15]/100) + a[25])
        self.EM = int(a[7] + a[17] + a[27])
        self.CR = round(a[5] + a[14] + a[24], 1)
        self.CD = round(a[4] + a[13] + a[23], 1)
        self.HB = round(a[9] + a[20] + a[30], 1)
        self.ER = round(a[8] + a[18] + a[28], 1)
        self.EDB = round(a[6] + a[16] + a[26], 1)
        self.PDB = round(a[10] + a[21] +a[31], 1)
    def get(self):
        arr = [self.BHP, self.HP, self.BATK, self.ATK, self.BDEF, self.DEF, self.EM, self.CR, self.CD, self.HB, self.ER, self.EDB, self.PDB]
        return arr

chara_list = ['Traveler', 'Keqing', 'Mona', 'Jean', 'Diluc', 'Qiqi', 'Venti', 'Klee', 'Tartaglia', 'Zhongli', 'Albedo', 'Ganyu', 'Xiao', 'Hu Tao', 'Eula', 'Kaedehara Kazuha', 'Kamisato Ayaka', 'Yoimiya', 'Raiden Shogun', 'Aloy', 'Sangonomia Kokomi', 'Arakati Itto', 'Shenhe', 'Yae Miko', 'Kamisato Ayato', 'Yelan']
wea_list = ["Skyward Harp", "Amos' Bow", "Elegy for the End", "Thundering Pulse", "Polar Star", "Aqua Simulacra", "Skyward Atlas", "Lost Prayer to the Sacred Winds", "Memory of Dust", "Everlasting Moonglow", "Kagura's Verity", "Skyward Spine", "Primordial Jade Winged-Spear", "Vortex Vanquisher", "Staff of Homa", "Engulfing Lightning", "Calamity Queller", "Skyward Pride", "Wolf's Gravestone", "The Unforged", "Song of Broken Pines", "Redhorn Stonethresher", "Skyward Blade", "Aquila Favonia", "Summit Shaper", "Primordial Jade Cutter", "Freedom-Sworn", "Mistsplitter Reforged", "Haran Geppaku Futsu"]

### 
print('Welcome to the game assistent system, lets begin!')
num = ['1st, 2nd 3rd, 4th']
words = ["Let's start by choosing the ", "Next, choose the ", "Moving on to the ", "Finally, key in the"]

print("Let's start by choosing the 1st character in you team setup!")
for i in chara_list:
    print(f"\t [{chara_list.index(i) + 1}] {i}")
Char1 = int(input('\n'))
Char1 = chara_list[Char1 - 1]
print(f'Your 1st character is: {Char1}')
Wea1 = characters[Char1].Weapon_Type
print(f'This character is using: {Wea1}')

wea_list1 = []
for i in wea_list:
    if (weapons[i].Type == Wea1):
        wea_list1.append(i)
print('Now, choose the weapon you want to equip for this character!\n')
for i in wea_list1:
    print(f"\t [{wea_list1.index(i) + 1}] {i}")
Wea1 = int(input('\n'))
Wea1 = wea_list1[Wea1 - 1]
print(f'The weapon equipped on your 1st character is: {Wea1}')          
    
artifacts1 = {}
for qn in qns:
    artifacts1[qn] = float(input(f"\nEnter your artifacts {qn} stat for {Char1}: \n"))
    artif = Art(artifacts1)
    artifacts1[Char1] = artif
    
        
Char1_attr = []
for i in Char_attr:
    Char1_attr.append(getattr(characters[f'{Char1}'], i))
for i in Wea_attr:
    Char1_attr.append(getattr(weapons[f'{Wea1}'], i))
for i in Art_attr:
    Char1_attr.append(getattr(artifacts1[f'{Char1}'], i))


team1 = team(Char1_attr)

###
print("Next choose the 2nd character in you team setup!")
for i in chara_list:
    print(f"\t [{chara_list.index(i) + 1}] {i}")
Char2 = int(input('\n'))
Char2 = chara_list[Char2 - 1]
print(f'Your 2nd character is: {Char2}')
Wea2 = characters[Char2].Weapon_Type
print(f'This character is using: {Wea2}')

wea_list2 = []
for i in wea_list:
    if (weapons[i].Type == Wea2):
        wea_list2.append(i)
print('Now, choose the weapon you want to equip for this character!\n')
for i in wea_list2:
    print(f"\t [{wea_list2.index(i) + 1}] {i}")
Wea2 = int(input('\n'))
Wea2 = wea_list2[Wea2 - 1]
print(f'The weapon equipped on your 2nd character is: {Wea2}')          
    
artifacts2 = {}
for qn in qns:
    artifacts2[qn] = float(input(f"\nEnter your artifacts {qn} stat for {Char2}: \n"))
    artif = Art(artifacts2)
    artifacts2[Char2] = artif
    
        
Char2_attr = []
for i in Char_attr:
    Char2_attr.append(getattr(characters[f'{Char2}'], i))
for i in Wea_attr:
    Char2_attr.append(getattr(weapons[f'{Wea2}'], i))
for i in Art_attr:
    Char2_attr.append(getattr(artifacts2[f'{Char2}'], i))


team2 = team(Char2_attr)

###
print("Moving on to the 3rd character in you team setup!")
for i in chara_list:
    print(f"\t [{chara_list.index(i) + 1}] {i}")
Char3 = int(input('\n'))
Char3 = chara_list[Char3 - 1]
print(f'Your 3rd character is: {Char3}')
Wea3 = characters[Char3].Weapon_Type
print(f'This character is using: {Wea3}')

wea_list3 = []
for i in wea_list:
    if (weapons[i].Type == Wea3):
        wea_list3.append(i)
print('Now, choose the weapon you want to equip for this character!\n')
for i in wea_list3:
    print(f"\t [{wea_list3.index(i) + 1}] {i}")
Wea3 = int(input('\n'))
Wea3 = wea_list3[Wea3 - 1]
print(f'The weapon equipped on your 3rd character is: {Wea3}')          
    
artifacts3 = {}
for qn in qns:
    artifacts3[qn] = float(input(f"\nEnter your artifacts {qn} stat for {Char3}: \n"))
    artif = Art(artifacts3)
    artifacts3[Char3] = artif
    
        
Char3_attr = []
for i in Char_attr:
    Char3_attr.append(getattr(characters[f'{Char3}'], i))
for i in Wea_attr:
    Char3_attr.append(getattr(weapons[f'{Wea3}'], i))
for i in Art_attr:
    Char3_attr.append(getattr(artifacts3[f'{Char3}'], i))


team3 = team(Char3_attr)

###
print("Finally, key in the 4th character in you team setup!")
for i in chara_list:
    print(f"\t [{chara_list.index(i) + 1}] {i}")
Char4 = int(input('\n'))
Char4 = chara_list[Char4 - 1]
print(f'Your 4th character is: {Char4}')
Wea4 = characters[Char4].Weapon_Type
print(f'This character is using: {Wea4}')

wea_list4 = []
for i in wea_list:
    if (weapons[i].Type == Wea4):
        wea_list4.append(i)
print('Now, choose the weapon you want to equip for this character!\n')
for i in wea_list4:
    print(f"\t [{wea_list4.index(i) + 1}] {i}")
Wea4 = int(input('\n'))
Wea4 = wea_list4[Wea4 - 1]
print(f'The weapon equipped on your 4th character is: {Wea4}')          
    
artifacts4 = {}
for qn in qns:
    artifacts4[qn] = float(input(f"\nEnter your artifacts {qn} stat for {Char4}: \n"))
    artif = Art(artifacts4)
    artifacts4[Char4] = artif
    
        
Char4_attr = []
for i in Char_attr:
    Char4_attr.append(getattr(characters[f'{Char4}'], i))
for i in Wea_attr:
    Char4_attr.append(getattr(weapons[f'{Wea4}'], i))
for i in Art_attr:
    Char4_attr.append(getattr(artifacts4[f'{Char4}'], i))


team4 = team(Char4_attr)

###
Base1 = ['Max HP', 'ATK', 'DEF']
Base2 = 'Elemental Mastery'
Advanced = ['CRIT Rate', 'CRIT DMG', 'Healing Bonus ', 'Energy Recharge']
Elemental = ['Elemetal DMG Bonus', 'Physical DMG Bonus']


Char1_attr = team1.get()
print(f'This is the characters Stats for {Char1} \n')
c1 = 0
print('Base Stats')
for i in Base1:
    l = 5 - len(i)//4 + 1
    print('\t', i, l*'\t', str(Char1_attr[c1]), '+', str(Char1_attr[c1+1]))
    c1 += 2
print('\t', Base2, '\t\t\t\t', str(Char1_attr[c1]))
c1 += 1
print('Advanced Stats')
for i in Advanced:
    l = 8 - len(i)//4 - 1
    print('\t', i, l*'\t', str(Char1_attr[c1]))
    c1 += 1
print('Elemental Type')
for i in Elemental:
    l = 9 - len(i)//4 - 1
    print('\t', i, l*'\t', str(Char1_attr[c1]))
    c1 += 1

###
Char2_attr = team2.get()
print(f'This is the characters Stats for {Char2} \n')
c2 = 0
print('Base Stats')
for i in Base1:
    l = 5 - len(i)//4 + 1
    print('\t', i, l*'\t', str(Char2_attr[c2]), '+', str(Char2_attr[c2+1]))
    c2 += 2
print('\t', Base2, '\t\t\t\t', str(Char2_attr[c2]))
c2 += 1
print('Advanced Stats')
for i in Advanced:
    l = 8 - len(i)//4 - 1
    print('\t', i, l*'\t', str(Char2_attr[c2]))
    c2 += 1
print('Elemental Type')
for i in Elemental:
    l = 9 - len(i)//4 - 1
    print('\t', i, l*'\t', str(Char2_attr[c2]))
    c2 += 1

###
Char3_attr = team3.get()
print(f'This is the characters Stats for {Char3} \n')
c3 = 0
print('Base Stats')
for i in Base1:
    l = 5 - len(i)//4 + 1
    print('\t', i, l*'\t', str(Char3_attr[c3]), '+', str(Char3_attr[c3+1]))
    c3 += 2
print('\t', Base2, '\t\t\t\t', str(Char3_attr[c3]))
c3 += 1
print('Advanced Stats')
for i in Advanced:
    l = 8 - len(i)//4 - 1
    print('\t', i, l*'\t', str(Char3_attr[c3]))
    c3 += 1
print('Elemental Type')
for i in Elemental:
    l = 9 - len(i)//4 - 1
    print('\t', i, l*'\t', str(Char3_attr[c3]))
    c3 += 1

###
Char4_attr = team4.get()
print(f'This is the characters Stats for {Char4} \n')
c4 = 0
print('Base Stats')
for i in Base1:
    l = 5 - len(i)//4 + 1
    print('\t', i, l*'\t', str(Char4_attr[c4]), '+', str(Char4_attr[c4+1]))
    c4 += 2
print('\t', Base2, '\t\t\t\t', str(Char4_attr[c4]))
c4 += 1
print('Advanced Stats')
for i in Advanced:
    l = 8 - len(i)//4 - 1
    print('\t', i, l*'\t', str(Char4_attr[c4]))
    c4 += 1
print('Elemental Type')
for i in Elemental:
    l = 9 - len(i)//4 - 1
    print('\t', i, l*'\t', str(Char4_attr[c4]))
    c4 += 1

