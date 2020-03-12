from random import choice
from bs4 import BeautifulSoup
from dataclasses import make_dataclass
from random import sample
from random import randint
from random import shuffle
from random import random
from pprint import pprint


import requests
import numpy as np


# URL = (
#     "https://portal.pzt.pl/TournamentAcceptanceList.aspx?CategoryID=AIS&"
#     "Male=&TournamentID=B038808C-6EA9-449B-AB82-6991104DA196"
# )
# TAG_NAME = "td"
# QUERY = ""
# response = requests.get(URL)
# content = response.content
# soup = BeautifulSoup(content, "html.parser")
# element = soup.find_all(TAG_NAME)

# def cook_soup():
#     URL = (
#     "https://portal.pzt.pl/TournamentAcceptanceList.aspx?CategoryID=AIS&"
#     "Male=&TournamentID=B038808C-6EA9-449B-AB82-6991104DA196"
#     )
#     TAG_NAME = "td"
#     QUERY = ""
#     response = requests.get(URL)
#     content = response.content
#     soup = BeautifulSoup(content, "html.parser")
#     element = soup.find_all(TAG_NAME)
#     return element
# element = cook_soup()


# def parse_soup(element):
#     string_data = {}
#     not_ranked = []
#     for i in range(0, len(element), 8):
#         first_name = element[i+2].text.strip()
#         last_name = element[i+3].text.strip()
#         ranking = element[i+7].text.strip()
#         if ranking.isdigit():
#             string_data[ranking] = {" ".join([first_name, last_name])}
#         else:
#             not_ranked.append(" ".join([first_name, last_name]))
#     for c, v in enumerate(not_ranked):
#         string_data[c + 10000] = v
#     return string_data
# data = parse_soup(element)
# print(data)

data = """


    1.  PAR1838041  Parszowski  Igor    1985-10-16  Niezrzeszony    świętokrzyskie  11
    2.  SOB1422291  Sobczyk Filip   1987-10-08  Niezrzeszony    podkarpackie    12
    3.  WRO1428864  Wrona   Jakub   1990-04-11  Niezrzeszony        13
    4.  TAK1419976  Takmadżan   Artem   1970-10-26  Niezrzeszony    podkarpackie    14
    5.  DAB1421837  Dąbrowski   Zbigniew    1972-10-06  Niezrzeszony    świętokrzyskie  15
    6.  WDO1426547  WDOWIAK TOMASZ  2004-09-11  Niezrzeszony    podkarpackie    
    7.  CAC1403410  Cach    Sebastian   1982-06-26  Niezrzeszony    podkarpackie    
    8.  CIA1632969  Ciak    Bartosz 1989-04-24  Niezrzeszony        
    9.  ZON1417549  Zontek  Tomasz  1977-10-10  Niezrzeszony    podkarpackie    
    10. DYB1837854  Dybka   Daniel  1973-10-19  Niezrzeszony    podkarpackie    
    11. MAC1737020  Maciej  Mateusz 1994-09-21  Niezrzeszony        
    12. KOZ1838119  Kozakiewicz Kamil   1976-06-18  Niezrzeszony    świętokrzyskie  
    13. PIA1418125  Piasta  Mariusz 1973-08-05  Niezrzeszony    mazowieckie 
    14. MAR1938061  Marszałek   Bartosz 2003-01-22  Klub Sportowy Czarni    podkarpackie    
    15. SIE1412859  Siek    Paweł   1979-08-25  Niezrzeszony    podkarpackie    
    16. KON2041089  Konopelski  Paweł   1975-12-30  Niezrzeszony    podkarpackie    
    17. BRE1414648  Breśka  Grzegorz    1966-11-20  Niezrzeszony    podkarpackie    
    18. DZI2041122  Dziki   Łukasz  1976-11-06  Niezrzeszony    podkarpackie    
    19. KLO2041248  Kłosowski   Szymon  2005-11-28  Niezrzeszony    podkarpackie    
     


    """

data2 = """

    1.  PAR1838041  Parszowski  Igor    1985-10-16  Niezrzeszony    świętokrzyskie  17
    2.  SOB1422291  Sobczyk Filip   1987-10-08  Niezrzeszony    podkarpackie    23
    3.  WRO1428864  Wrona   Jakub   1990-04-11  Niezrzeszony        41
    4.  TAK1419976  Takmadżan   Artem   1970-10-26  Niezrzeszony    podkarpackie    67
    5.  DAB1421837  Dąbrowski   Zbigniew    1972-10-06  Niezrzeszony    świętokrzyskie  71
    6.  WDO1426547  WDOWIAK TOMASZ  2004-09-11  Niezrzeszony    podkarpackie    75
    7.  CAC1403410  Cach    Sebastian   1982-06-26  Niezrzeszony    podkarpackie    90
    8.  CIA1632969  Ciak    Bartosz 1989-04-24  Niezrzeszony        93
    9.  ZON1417549  Zontek  Tomasz  1977-10-10  Niezrzeszony    podkarpackie    99
    10. DYB1837854  Dybka   Daniel  1973-10-19  Niezrzeszony    podkarpackie    105
    11. MAC1737020  Maciej  Mateusz 1994-09-21  Niezrzeszony        105
    12. KOZ1838119  Kozakiewicz Kamil   1976-06-18  Niezrzeszony    świętokrzyskie  112
    13. PIA1418125  Piasta  Mariusz 1973-08-05  Niezrzeszony    mazowieckie 118
    14. MAR1938061  Marszałek   Bartosz 2003-01-22  Klub Sportowy Czarni    podkarpackie    125
    15. SIE1412859  Siek    Paweł   1979-08-25  Niezrzeszony    podkarpackie    127
    16. KON2041089  Konopelski  Paweł   1975-12-30  Niezrzeszony    podkarpackie    142
    17. BRE1414648  Breśka  Grzegorz    1966-11-20  Niezrzeszony    podkarpackie    156
    18. DZI2041122  Dziki   Łukasz  1976-11-06  Niezrzeszony    podkarpackie    156
    19. KLO2041248  Kłosowski   Szymon  2005-11-28  Niezrzeszony    podkarpackie    156
    20. MAC2041251  Maciej  Damian  1990-11-30  Niezrzeszony    podkarpackie    156
    21. WOJ2041110  Wojtanowski Adrian  2001-05-27  Niezrzeszony    podkarpackie    156
    22. ZAG1407230  Zagórowski  Andrzej 1955-01-02  Niezrzeszony    lubelskie   156
    23. SZE2041097  Szeliga Robert  1977-05-12  Niezrzeszony    podkarpackie    163
    24. FOL2041050  Folfas  Andrzej 1976-03-26  Niezrzeszony    świętokrzyskie  189
    25. ALI2041394  Alivand Amin    1985-03-06  Niezrzeszony    mazowieckie 
    26. BOR2041428  Borkowski   Jacek   1967-09-22  Niezrzeszony    podkarpackie    
    27. GUM1404921  Gumuliński  Jakub   1983-03-14  Niezrzeszony    mazowieckie 
    28. KIS2041400  Kisiel  Bartosz 2006-07-14  Niezrzeszony    podkarpackie    
    29. MIC2041160  Michalewski Albert  1963-07-06  Niezrzeszony        
    30. ROG1938482  Rogus   Miłosz  2004-01-14  Niezrzeszony    podkarpackie    
    31. ROM2041288  Roman   Jakub   2002-02-03  Niezrzeszony        

"""


data4 = """


    1.  DRE1839104  Drela   Zuzanna 2001-12-11  Stowarzyszenie AG TENIS CHORZOWSKA w Radomiu    mazowieckie 2
    2.  GRE1938822  Gregorczyk  Gabriela    2005-10-13  Niezrzeszony    mazowieckie 3
    3.  OST1939810  Ostrowska   Monika  1986-05-30  Niezrzeszony        8
    4.  CHR1403701  Chrzanowska-Szczygielska    Nina    1981-12-14  Niezrzeszony    podkarpackie    9
    5.  SUC2041108  Suchy   Wiktoria    2000-11-10  Niezrzeszony    podkarpackie    21
    6.  SZE2041101  Szeliga Agnieszka   1977-05-30  Niezrzeszony    podkarpackie    22
    7.  CZE2041099  Czerwińska  Natalia 1999-08-13  Niezrzeszony    podkarpackie    25
    8.  SOL2041250  Sołek   Joanna  2003-05-30  Niezrzeszony    podkarpackie    


"""

def parse(data):
    players_data = {}
    data = data.strip().splitlines()
    name_idx, rank_idx = [2, 3], [6, 7]
    seed_players = 0
    for idx, line in enumerate(data):
        name = []
        rank = 0
        for c, v in enumerate(line.split()):
            if c in name_idx:
                name.append(v.title())
            elif c in rank_idx:
                if v.isdigit():
                    rank = int(v)
                    seed_players += 1
        players_data[idx + 1] = [' '.join(name), rank]
    return players_data, seed_players

data, seed_players = parse(data)


def cup_pairs(tournament_size):
    if tournament_size == 16:
        pairs = {1: {1: '', 2: ''}, 2: {16: '', 15: ''}}
        shuffle = [{5: '', 6: ''}, {12: '', 11: ''}]
        choice_indices = np.random.choice(
            len(shuffle), len(shuffle), replace=False,
        )
        for idx in choice_indices:
            next_key = list(pairs.keys())[-1] + 1
            pairs[next_key] = shuffle[idx]
    elif tournament_size == 32:
        pairs = {1: {1: '', 2: ''}, 2: {32: '', 31: ''}}
        shuffle1 = [{9: '', 10: ''}, {24: '', 23: ''}]
        shuffle2 = [
            {8: '', 7: ''}, {16: '', 15: ''}, {17: '', 18: ''}, 
            {25: '', 26: ''}
        ]
        choice_indices = np.random.choice(
            len(shuffle1), len(shuffle1), replace=False,
        )
        for idx in choice_indices:
            next_key = list(pairs.keys())[-1] + 1
            pairs[next_key] = shuffle1[idx]
        choice_indices = np.random.choice(
            len(shuffle2), len(shuffle2), replace=False,
        )
        for idx in choice_indices:
            next_key = list(pairs.keys())[-1] + 1
            pairs[next_key] = shuffle2[idx]
    elif tournament_size == 8:
        return print('Not ready yet')
    used_positions = []
    for val in pairs.values():
        for key in val:
            used_positions.append(key)
    for i in range(1, tournament_size + 1, 2):
        if i not in used_positions and i+1 not in used_positions:
            next_key = list(pairs.keys())[-1] + 1
            pairs[next_key] = {i: '', i+1: ''}
    return pairs

pairs = cup_pairs(32)


def get_pairs(data, pairs, tournament_size, tounrament_type, seed_players):
    players_done = 0
    if seed_players > tournament_size // 4:
        seed_players = tournament_size // 4
    byes_needed = tournament_size - len(data)
    pairs_lst = []
    unfilled_pairs = []
    left_data_keys = list(data.keys())
    for c, v in enumerate(pairs, 1):
        first_pairs_key = list(pairs[c].keys())[0]
        second_pairs_key = list(pairs[c].keys())[1]
        if seed_players > 0:
            if byes_needed > 0:
                pairs[c][first_pairs_key] = data[c]
                pairs[c][second_pairs_key] = 'BYE'
                left_data_keys.remove(c)
                seed_players -= 1
                byes_needed -= 1
            else:
                pairs[c][first_pairs_key] = data[c]
                random_key = choice(left_data_keys[c+1:])
                pairs[c][second_pairs_key] = data[random_key]
                left_data_keys.remove(c)
                left_data_keys.remove(random_key)
                seed_players -= 1
                continue
        if seed_players == 0 and len(left_data_keys) > 0:
            unfilled_pairs.append(c+1)           
            if byes_needed > 0:
                r1 = choice(left_data_keys)
                pairs_lst.append([data[r1], ['BYE', 0]])
                left_data_keys.remove(r1)
                byes_needed -= 1
            else:
                r1 = choice(left_data_keys)
                left_data_keys.remove(r1)
                r2 = choice(left_data_keys)
                left_data_keys.remove(r2)
                pairs_lst.append([data[r1], data[r2]])
    unfilled_pairs_idx = 0
    for key, val in pairs.items():
        if key in unfilled_pairs:
            first_pairs_key = list(val)[0]
            second_pairs_key = list(val)[1]
            first_pair = pairs_lst[unfilled_pairs_idx][0]
            second_pair = pairs_lst[unfilled_pairs_idx][1]
            unfilled_pairs_idx += 1
            pairs[key][first_pairs_key] = first_pair
            pairs[key][second_pairs_key] = second_pair
    pprint(pairs)

get_pairs(data, pairs, 32, "cup", seed_players)