from random import randint
from bs4 import BeautifulSoup


import requests
import numpy as np


def html_find(url, tag_name, query):
    URL = url
    TAG_NAME = tag_name
    QUERY = query
    response = requests.get(URL)
    content = response.content
    soup = BeautifulSoup(content, "html.parser")
    return soup.find_all(TAG_NAME)
     
search_result = html_find(
    url=(
        "https://portal.pzt.pl/TournamentAcceptanceList.aspx?CategoryID=10&"
        "Male=&TournamentID=20596A85-0C43-4713-B577-FFCF9E68A958"
    ),
    tag_name="td",
    query={"class": "r"},
)

to_parse = ['1.', 'CHM1838401', 'Chmielewski', 'Jakub', '2010-08-27', 'Niezrzeszony', '2.', 'GAJ1839129', 'GAJDA', 'KSAWERY', '2010-01-21', 'RKT Return Radom', 'mazowieckie', '3.', 'KOW1938339', 'Kowalik', 'Wojciech', '2010-05-28', 'KS Nadwiślan Kraków', 'małopolskie', '2', '4.', 'KRZ1940892', 'Krzystolik', 'Konrad', '2010-12-17', 'Śląskie Centrum Tenisa Pszczyna', 'śląskie', '5.', 'PRE1635109', 'Preisner', 'Aleksander', '2010-03-28', 'Niezrzeszony', 'podkarpackie', '1', '6.', 'ROJ1940360', 'Rojewski', 'Kacper', '2011-08-29', 'Sport Klub Kryspinów', 'małopolskie', '7.', 'ZYG2041184', 'Zyguła', 'Aleksander', '2011-01-08', 'Klub Tenisowy Błonia Kraków', 'małopolskie', '3', 'out_of_range_error_fix']

def read_soup(html_find_results):
    to_parse = []
    for c, v in enumerate(html_find_results):
      if len(v.text.strip()) >= 1:
          to_parse.append(v.text.strip())
    to_parse.append('out_of_range_error_fix')
    return to_parse

#to_parse = read_soup(html_find_results=search_result)


def parse(data):
    lp_list = [f"{i}." for i in range(1, 65)]
    data_list = []
    for c, v in enumerate(data):
        append_to_data = []
        if v in lp_list:
            name = ' '.join([str(data[c+2]), str(data[c+3])])
            append_to_data.append(name.title())
            if data[c+7].isdigit():
                append_to_data.append(data[c+7])
            if data[c+6].isdigit():
                append_to_data.append(data[c+6])    
        if len(append_to_data) >= 1:
            data_list.append(append_to_data)
    return data_list

data = parse(to_parse)

def ladder_places(tournament_size):
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
ladder_places(tournament_size=16)



def get_pairs(tournament_size, players_list):
    players_positions = ladder_places(tournament_size)
    seed_players_number = 0
    for player_data in players_list:
        if len(player_data) > 1:
            seed_players_number += 1
    for i in range(tournament_size - len(players_list)):
        players_list.append(['BYE'])
    players_sorted = sorted(players_list, key=lambda x: x[-1])
    pairs = {}
    position_used = 0
    randoms = list(range(tournament_size))
    print(randoms)
    for c, v in enumerate(players_sorted):
        print(c, v)
        if c < seed_players_number:
            pairs[players_positions[c]] = {tuple(v): 'BYE'}
            position_used += 1
            randoms.pop(c)
        else:
            while len(players_sorted) > 0:
                r1 = players_sorted[randint(0, randoms)]
                randoms.remove
                r2 = players_sorted[randint(0, randoms)]
                r1 = r1[0]
                r2 = r2[0]
                print(r1)
                print(r2)
                if r1 == ['BYE']:
                    pairs[c] = {r2: r1}
                else:
                    pairs[c] = {r1: r2}
    print(pairs)



get_pairs(
    tournament_size=16, 
    players_list=data, 
)