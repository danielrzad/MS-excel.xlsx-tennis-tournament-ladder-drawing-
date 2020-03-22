from random import choice
from dataclasses import make_dataclass
from random import random
from pprint import pprint


import settings
import requests
import numpy as np


def parse(data_path, tournament_size):
    data = data_path.read_text()
    players_data = {}
    PlayersAttributes = make_dataclass(
       "PlayersAttributes", ["name", "rank", "seed", "second_round"]
    )
    data = data.strip().splitlines()
    name_idx, rank_idx = [2, 3], [6, 7]
    seed_players = 0
    for idx, line in enumerate(data, 1):
        name = []
        rank = 0
        seed = 0
        for c, v in enumerate(line.split()):
            if c in name_idx:
                name.append(v.title())
            elif c in rank_idx:
                if v.isdigit():
                    rank = int(v)
                    if idx <= tournament_size // 4:
                        seed_players += 1
                        seed = idx
        name = " ".join(name)
        players_data[idx] = PlayersAttributes(
            name=name, rank=rank, seed=seed, second_round=0
        )
    return players_data, seed_players


data, seed_players = parse(
    data_path=settings.paths["players_data_path"],
    tournament_size=settings.config["tournament_size"],
)


def cup_pairs(tournament_size):
    if tournament_size == 8:
        pairs = {1: {1: '', 2: ''}, 2: {8: '', 7: ''}}
    elif tournament_size == 16:
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
    used_positions = []
    for val in pairs.values():
        for key in val:
            used_positions.append(key)
    for i in range(1, tournament_size + 1, 2):
        if i not in used_positions and i+1 not in used_positions:
            next_key = list(pairs.keys())[-1] + 1
            pairs[next_key] = {i: '', i+1: ''}
    return pairs


pairs = cup_pairs(settings.config["tournament_size"])


def get_pairs(data, pairs, tournament_size, tounrament_type, seed_players):
    Bye = make_dataclass(
       "Bye", ["name", "rank", "seed", "second_round"]
    )
    bye = Bye(
        name="Bye", rank=0, seed=0, second_round=0
    )
    players_done = 0
    byes_needed = tournament_size - len(data)
    pairs_lst = []
    unfilled_pairs = []
    left_data_keys = list(data.keys())
    for c, v in enumerate(pairs, 1):
        first_pairs_key = list(pairs[c].keys())[0]
        second_pairs_key = list(pairs[c].keys())[1]
        if seed_players > 0:
            if byes_needed > 0:
                data[c].second_round = 1
                pairs[c][first_pairs_key] = data[c]
                pairs[c][second_pairs_key] = bye
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
            unfilled_pairs.append(c)           
            if byes_needed > 0:
                r1 = choice(left_data_keys)
                data[r1].second_round = 1
                pairs_lst.append([data[r1], bye])
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
    return pairs

players_placement = get_pairs(
    data=data,
    pairs=pairs,
    tournament_size=settings.config["tournament_size"],
    tounrament_type=settings.config["tournament_type"],
    seed_players=seed_players,
    )
