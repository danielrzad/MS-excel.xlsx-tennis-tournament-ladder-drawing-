from random import randint
from bs4 import BeautifulSoup
2, 3 , 

import requests
import numpy as np

URL = (
    "https://portal.pzt.pl/TournamentAcceptanceList.aspx?CategoryID=AIS&"
    "Male=&TournamentID=B038808C-6EA9-449B-AB82-6991104DA196"
)
TAG_NAME = "td"
QUERY = ""
response = requests.get(URL)
content = response.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find_all(TAG_NAME)

def cook_soup():
    URL = (
    "https://portal.pzt.pl/TournamentAcceptanceList.aspx?CategoryID=AIS&"
    "Male=&TournamentID=B038808C-6EA9-449B-AB82-6991104DA196"
    )
    TAG_NAME = "td"
    QUERY = ""
    response = requests.get(URL)
    content = response.content
    soup = BeautifulSoup(content, "html.parser")
    element = soup.find_all(TAG_NAME)
    return element
element = cook_soup()


def parse_soup(element):
    string_data = {}
    not_ranked = []
    for i in range(0, len(element), 8):
        first_name = element[i+2].text.strip()
        last_name = element[i+3].text.strip()
        ranking = element[i+7].text.strip()
        if ranking.isdigit():
            string_data[ranking] = {" ".join([first_name, last_name])}
        else:
            not_ranked.append(" ".join([first_name, last_name]))
    for c, v in enumerate(not_ranked):
        string_data[c + 10000] = v
    return string_data
data = parse_soup(element)
print(data)

def cup_places(tournament_size):
    if tournament_size == 16:
        players_positions = [1, 16]
        used = [1, 16, 5, 12]
        l3 = [i for i in range(1, 17) if i not in used]
        ladder = [[5, 12], [2, 3, 4, 6, 7, 8, 9, 10, 11, 13, 14, 15]]
        for l in ladder:
            l = np.random.choice(l, len(l), False,)
            for i in l:
                players_positions.append(i)
    elif tournament_size == 32:
        players_positions = [1, 32]
        l2 = [10, 24]
        l3 = [18, 16, 17, 25]
        used = [1, 32] + l2 + l3
        l4 = [i for i in range(1, 33) if i not in used]
        ladder = [l2, l3, l4]
        for l in ladder:
            l = np.random.choice(l, len(l), False,)
            for i in l:
                players_positions.append(i)
    return players_positions

players_positions = cup_places(32)
print(players_positions)




def get_pairs(data, players_positions, tournament_size, tounrament_type):
    seed_players = tournament_size // 4
    players_sorted = sorted(data.keys())
    print(players_sorted)


get_pairs(data, players_positions, 32, "cup")



# def get_pairs(tournament_size, players_list):
#     players_positions = ladder_places(tournament_size)
#     seed_players_number = 0
#     for player_data in players_list:
#         if len(player_data) > 1:
#             seed_players_number += 1
#     for i in range(tournament_size - len(players_list)):
#         players_list.append(['BYE'])
#     players_sorted = sorted(players_list, key=lambda x: x[-1])
#     pairs = {}
#     position_used = 0
#     randoms = list(range(tournament_size))
#     print(randoms)
#     for c, v in enumerate(players_sorted):
#         print(c, v)
#         if c < seed_players_number:
#             pairs[players_positions[c]] = {tuple(v): 'BYE'}
#             position_used += 1
#             randoms.pop(c)
#         else:
#             while len(players_sorted) > 0:
#                 r1 = players_sorted[randint(0, randoms)]
#                 randoms.remove
#                 r2 = players_sorted[randint(0, randoms)]
#                 r1 = r1[0]
#                 r2 = r2[0]
#                 print(r1)
#                 print(r2)
#                 if r1 == ['BYE']:
#                     pairs[c] = {r2: r1}
#                 else:
#                     pairs[c] = {r1: r2}
#     print(pairs)



# get_pairs(
#     tournament_size=16, 
#     players_list=data, 
# )