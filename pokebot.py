#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 09:15:29 2021

@author: jamison
"""
import numpy as np
import pandas as pd
import os

pokemon_df = pd.read_csv('pokemon_info.csv')
pokemon_df = pokemon_df.set_index('name')
pokemon_df[['weight_kg']] = pokemon_df[['weight_kg']].fillna(1)
pokemon_df[['speed']] = pokemon_df[['speed']].fillna(1)
pokemon_df['dexterity']=pokemon_df['speed']/pokemon_df['weight_kg']
forbidden_names =['Nidoran-f', 'Nidoran-m', "Farfetchd", 'Type-Null']
def forbidden_names_index(name):
    if name == 'Nidoran-f':
        name = 'Nidoran♀'
    if name == 'Nidoran-m':
        name = 'Nidoran♂'
    if name == 'Farfetchd':
        name = 'Farfetch\'d'
    if name == 'Type-null':
        name = 'Type: Null'
    return name

def attack(attacker, defender):
    attacker = attacker.strip()
    defender = defender.strip()
    attack = np.random.choice(eval(pokemon_df.loc[attacker]['abilities']))
    hits = np.random.choice([0,1], p=[.25,.75])
    if hits == 0:
        return (attack, hits)
    else:
        def_t1 = pokemon_df.loc[defender]['type1']
        def_t2 = pokemon_df.loc[defender]['type2']
        if type(def_t2) == float:
            def_t2 = def_t1
        if def_t1 == 'fighting':
            def_t1 = 'fight'
        if def_t2 == 'fighting':
            def_t2 = 'fight'
        damage_mult = 2 - (pokemon_df.loc[attacker]['against_'+ def_t1]*(0.5) + pokemon_df.loc[attacker]['against_'+ def_t2]*(0.5))
        damage_mult = max(0, damage_mult)
        attack_damage = np.random.randint(10,31)
        damage = ((0.75) * damage_mult + (0.25)) * attack_damage
        return (attack, hits, int(damage))

#play
'''
choice1 = 'Mewtwo'
choice2 = 'Kingler'

p1, p2 = play_order(choice1, choice2)
hp1 = np.random.randint(50,101)
hp2 = np.random.randint(50,101)
hp_dict = {p1: hp1, p2: hp2}
print(f'{p1} versus {p2}')
print(f'{p1} has {hp1} hp. {p2} has {hp2} hp.')
time.sleep(2)
while hp_dict[p1] > 0:
    hit_tup = attack(p1, p2)
    if len(hit_tup) == 2:
        print(f'{p1} uses {hit_tup[0]} and misses!')
        p1, p2 = p2, p1
    else:
        print(f'{p1} uses {hit_tup[0]} and hits! {p1} deals {hit_tup[2]} damage!')
        hp_dict[p2] -= hit_tup[2]
        p1, p2 = p2, p1
    print(f'{p1} has {max(hp_dict[p1], 0)} hp. {p2} has {max(hp_dict[p2], 0)} hp.')
    time.sleep(2)
print(f'{p2} is the victor!')'''

def get_pic_path(pokemon):
    pokemon = pokemon.casefold().replace('.','').replace(' ','-').replace('\'','').replace(':','').replace('♂','-m').replace('♀','-f')
    poke_pic_list = os.listdir('pokemon_images')
    pic_name = pokemon + '.png'
    if pic_name in poke_pic_list:
        pic_name = pic_name
    elif pokemon + '.jpg' in poke_pic_list:
        pic_name = pokemon + '.jpg'
    else:
        return
    
    return 'pokemon_images/' + pic_name

def random_pokemon():
    p = pokemon_df.index[np.random.randint(1,802)]
    return p
    
    
