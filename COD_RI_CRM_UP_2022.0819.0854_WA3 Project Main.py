import csv
import sys
import time

def sprint(inp):
    '''print out the input string character by character with a time interval of 0.03 seconds'''
    for ch in inp:
        # takes a single character of the string
        sys.stdout.write(ch)
            # set the character as the display to terminal
        sys.stdout.flush()
            # force the previous step to write to terminal immediately
        time.sleep(0.03)
            # wait for 0.03 seconds 
    sys.stdout.write('\n')
        # make sure the next print() starts from a new line

def fprint(inp):
    '''print out the input string character by character with a time interval of 0.005 seconds'''
    for ch in inp:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(0.005)
            # wait for 0.005 seconds
    sys.stdout.write('\n')

class Cha:
    '''Character class that stores all the character information'''
    def __init__(self, att):
        '''takes in a dictionary and set the key as the object name, value as the corresponding object value'''
        for a, b in att.items():
            a = a.replace(" ", "_")
            a = a.replace("%", "p")
                # ensure that the names from the csv files are renamed properly based on python rules
            self.__setattr__(a, b)

characters = {}
    # a dictionary that is used to store all the character data

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
    '''Weapon class that stores all the weapon information'''
    def __init__(self, att):
        for a, b in att.items():
            a = a.replace(" ", "1")
                # use a different way to rename to differentiate the name from that of Character class
            a = a.replace("%", "P")
            a = a.replace("Rarity", "Rarity1")
            self.__setattr__(a, b)

weapons = {}
    # a dictionary that stores all the weapon data

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
    '''Artifacts class that stores all the artifacts information'''
    def __init__(self, att):
        for a, b in att.items():
            a = a.replace(" ", "2")
            self.__setattr__(a, b)

qns = ["HP","ATK","DEF","Elemental Mastery","CRIT Rate","CRIT DMG","Healing Bonus","Energy Recharge","Elemental DMG Bonus","Physical DMG Bonus"]
    # a list of questions that will be used for user input
Char_attr = ['ATKp', 'Base_ATK', 'Base_DEF', 'Base_HP', 'CRIT_DMG', 'CRIT_Rate', 'Elemental_DMG_Bonus', 'Elemental_Mastery', 'Energy_Recharge', 'Healing_Bonus', 'Physical_DMG_Bonus']
    # a list of object names from the Character class
Wea_attr = ['ATKP', 'Base1ATK', 'CRIT1DMG', 'CRIT1Rate', 'DEFP', 'Elemental1DMG1Bonus', 'Elemental1Mastery', 'Energy1Recharge', 'HPP', 'Healing1Bonus', 'Physical1DMG1Bonus']
    # a list of object names from the Weapon class
Art_attr = ['ATK', 'CRIT2DMG', 'CRIT2Rate', 'DEF', 'Elemental2DMG2Bonus', 'Elemental2Mastery', 'Energy2Recharge', 'HP', 'Healing2Bonus', 'Physical2DMG2Bonus']
    # a list of object names from Artifacts class

class team:
    '''Team class that stores the calculated value of the characters of the team'''
    def __init__(self, a):
        '''takes the list of the raw attributes in a particular order and set them as new attibutes after calculation'''
        self.BATK = int(a[1] + a[12])
        self.ATK = int((a[1] + a[12]) * (a[0]/100 + a[11]/100) + a[22])
        self.BHP = int(a[3])
        self.HP = int(a[3] * (a[19]/100) + a[29])
        self.BDEF = int(a[2])
        self.DEF = int(a[2] * (a[15]/100) + a[25])
        self.EM = int(a[7] + a[17] + a[27])
            # only take the integer part for the above attributes
        self.CR = round(a[5] + a[14] + a[24], 1)
        self.CD = round(a[4] + a[13] + a[23], 1)
        self.HB = round(a[9] + a[20] + a[30], 1)
        self.ER = round(a[8] + a[18] + a[28], 1)
        self.EDB = round(a[6] + a[16] + a[26], 1)
        self.PDB = round(a[10] + a[21] +a[31], 1)
            # round the above value to 1 decimal point
    def get(self):
        ''' access and return all the attributes as a list'''
        arr = [self.BHP, self.HP, self.BATK, self.ATK, self.BDEF, self.DEF, self.EM, self.CR, self.CD, self.HB, self.ER, self.EDB, self.PDB]
            # return the value in the particular order
        return arr

chara_list = ['Traveler', 'Keqing', 'Mona', 'Jean', 'Diluc', 'Qiqi', 'Venti', 'Klee', 'Tartaglia', 'Zhongli', 'Albedo', 'Ganyu', 'Xiao', 'Hu Tao', 'Eula', 'Kaedehara Kazuha', 'Kamisato Ayaka', 'Yoimiya', 'Raiden Shogun', 'Aloy', 'Sangonomia Kokomi', 'Arakati Itto', 'Shenhe', 'Yae Miko', 'Kamisato Ayato', 'Yelan']
    # a list of all the characters for user's choice
wea_list = ["Skyward Harp", "Amos' Bow", "Elegy for the End", "Thundering Pulse", "Polar Star", "Aqua Simulacra", "Skyward Atlas", "Lost Prayer to the Sacred Winds", "Memory of Dust", "Everlasting Moonglow", "Kagura's Verity", "Skyward Spine", "Primordial Jade Winged-Spear", "Vortex Vanquisher", "Staff of Homa", "Engulfing Lightning", "Calamity Queller", "Skyward Pride", "Wolf's Gravestone", "The Unforged", "Song of Broken Pines", "Redhorn Stonethresher", "Skyward Blade", "Aquila Favonia", "Summit Shaper", "Primordial Jade Cutter", "Freedom-Sworn", "Mistsplitter Reforged", "Haran Geppaku Futsu"]
    # a list of all the weapons for user's choice
team_list = ['1st', '2nd', '3rd', '4th']
    # a list for the programme to iterate through
### 
sprint("Welcome to the game assistent system, let's begin!")
for t in team_list:
    if t == '1st':
        sprint("Let's start by choosing the 1st character in you team setup!")
    elif t == '2nd':
        sprint("\n\nNext choose the 2nd character in you team setup!")
    elif t == '3rd':
        sprint("\n\nMoving on to the 3rd character in you team setup!")
    elif t == '4th':
        sprint("\n\nFinally, key in the 4th character in you team setup!")
    sprint('Enter the character index number of your choice\n')
    for i in chara_list:
        fprint(f"\t [{chara_list.index(i) + 1}] {i}")
    while True:  
        try:
            Char1 = int(input())
            if Char1 <= 0:
                raise ValueError('Please enter a postive number from 1 to {len(chara_list)}')
            Char1 = chara_list[Char1 - 1]
        except ValueError:
            print(f'\nValueError! Please enter an integer value from 1 to {len(chara_list)}')
        except IndexError:
            print(f'\nIndexError! Please enter an integer value from 1 to {len(chara_list)}')
        else:
            break
    sprint(f'Your {t} character is: {Char1}')
    Wea1 = characters[Char1].Weapon_Type
    sprint(f'This character is using: {Wea1}')
    wea_list1 = []
    for i in wea_list:
        if (weapons[i].Type == Wea1):
            wea_list1.append(i)
    sprint('Now, choose the weapon you want to equip for this character!')
    sprint('Enter the weapon index number of your choice\n')
    for i in wea_list1:
        fprint(f"\t [{wea_list1.index(i) + 1}] {i}")
    while True:  
        try:
            Wea1 = int(input())
            if Wea1 <= 0:
                raise ValueError('Please enter a postive number from 1 to {len(wea_list1)}')
            Wea1 = wea_list1[Wea1 - 1]
        except ValueError:
            print(f'\nValueError! Please enter an integer value from 1 to {len(wea_list1)}')
        except IndexError:
            print(f'\nIndexError! Please enter an integer value from 1 to {len(wea_list1)}')
        else:
            break
    sprint(f'The weapon equipped on your {t} character is: {Wea1}')
    sprint('Moving on to the artifacts Stats\n-> you may enter "r" to redo the previous stats entry\n-> you may click "enter" to skip a stat entry, 0 will be automatically assigned.')
    artifacts1 = {}
    a1 = 0
    while a1 < len(qns):
        fprint(f"\nEnter your artifacts {qns[a1]} stat for {Char1}:")
        while True:
            ans = input()
            if ans == 'r':
                a1 -= 2
                break
            elif ans == '':
                artifacts1[qns[a1]] = 0.0
                artif = Art(artifacts1)
                artifacts1[Char1] = artif
                break
            else:
                try: 
                    artifacts1[qns[a1]] = float(ans)
                    artif = Art(artifacts1)
                    artifacts1[Char1] = artif
                except ValueError:
                    print(f'\nValueError! Please enter a floating point value or an integer value')
                else:
                    break
        a1 += 1
    Char1_attr = []
    for i in Char_attr:
        Char1_attr.append(getattr(characters[f'{Char1}'], i))
    for i in Wea_attr:
        Char1_attr.append(getattr(weapons[f'{Wea1}'], i))
    for i in Art_attr:
        Char1_attr.append(getattr(artifacts1[f'{Char1}'], i))
    if t == '1st':
        team1 = team(Char1_attr)
        t1 = Char1
    elif t == '2nd':
        team2 = team(Char1_attr)
        t2 = Char1
    elif t == '3rd':
        team3 = team(Char1_attr)
        t3 = Char1
    elif t == '4th':
        team4 = team(Char1_attr)
        t4 = Char1

for o in range(4):
    if o == 0:
        Char1_attr = team1.get()
        out1 = f"""
    This is the character Stats for {t1}
    Base Stats:
        Max HP\t\t\t\t\t{Char1_attr[0]} + {Char1_attr[1]}
        ATK\t\t\t\t\t{Char1_attr[2]} + {Char1_attr[3]}
        DEF\t\t\t\t\t{Char1_attr[4]} + {Char1_attr[5]}
        Elemental Mastery\t\t\t{Char1_attr[6]}
    Advanced Stats:
        CRIT Rate\t\t\t\t{Char1_attr[7]}
        CRIT DMG\t\t\t\t{Char1_attr[8]}
        Healing Bonus\t\t\t\t{Char1_attr[9]}
        Energy Recharge\t\t\t\t{Char1_attr[10]}
    Elemental Type:
        Elemental DMG Bonus\t\t\t{Char1_attr[11]}
        Physical DMG Bonus\t\t\t{Char1_attr[12]}
    """
    elif o == 1:
        Char1_attr = team2.get()
        out2 = f"""
    This is the character Stats for {t2}
    Base Stats:
        Max HP\t\t\t\t\t{Char1_attr[0]} + {Char1_attr[1]}
        ATK\t\t\t\t\t{Char1_attr[2]} + {Char1_attr[3]}
        DEF\t\t\t\t\t{Char1_attr[4]} + {Char1_attr[5]}
        Elemental Mastery\t\t\t{Char1_attr[6]}
    Advanced Stats:
        CRIT Rate\t\t\t\t{Char1_attr[7]}
        CRIT DMG\t\t\t\t{Char1_attr[8]}
        Healing Bonus\t\t\t\t{Char1_attr[9]}
        Energy Recharge\t\t\t\t{Char1_attr[10]}
    Elemental Type:
        Elemental DMG Bonus\t\t\t{Char1_attr[11]}
        Physical DMG Bonus\t\t\t{Char1_attr[12]}
    """
    elif o == 2:
        Char1_attr = team3.get()
        out3 = f"""
    This is the character Stats for {t3}
    Base Stats:
        Max HP\t\t\t\t\t{Char1_attr[0]} + {Char1_attr[1]}
        ATK\t\t\t\t\t{Char1_attr[2]} + {Char1_attr[3]}
        DEF\t\t\t\t\t{Char1_attr[4]} + {Char1_attr[5]}
        Elemental Mastery\t\t\t{Char1_attr[6]}
    Advanced Stats:
        CRIT Rate\t\t\t\t{Char1_attr[7]}
        CRIT DMG\t\t\t\t{Char1_attr[8]}
        Healing Bonus\t\t\t\t{Char1_attr[9]}
        Energy Recharge\t\t\t\t{Char1_attr[10]}
    Elemental Type:
        Elemental DMG Bonus\t\t\t{Char1_attr[11]}
        Physical DMG Bonus\t\t\t{Char1_attr[12]}
    """
    elif o == 3:
        Char1_attr = team4.get()
    out4 = f"""
    This is the character Stats for {t4}
    Base Stats:
        Max HP\t\t\t\t\t{Char1_attr[0]} + {Char1_attr[1]}
        ATK\t\t\t\t\t{Char1_attr[2]} + {Char1_attr[3]}
        DEF\t\t\t\t\t{Char1_attr[4]} + {Char1_attr[5]}
        Elemental Mastery\t\t\t{Char1_attr[6]}
    Advanced Stats:
        CRIT Rate\t\t\t\t{Char1_attr[7]}
        CRIT DMG\t\t\t\t{Char1_attr[8]}
        Healing Bonus\t\t\t\t{Char1_attr[9]}
        Energy Recharge\t\t\t\t{Char1_attr[10]}
    Elemental Type:
        Elemental DMG Bonus\t\t\t{Char1_attr[11]}
        Physical DMG Bonus\t\t\t{Char1_attr[12]}
    """
fprint(out1)
fprint(out2)
fprint(out3)
fprint(out4)
