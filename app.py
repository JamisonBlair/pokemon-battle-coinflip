import pandas as pd
import streamlit as st
import pokebot
import numpy as np
import time


pokemon_df = pd.read_csv("pokemon_info.csv")

names = pokemon_df['name'].values

pokemon1 = st.selectbox('Player 1 Choose Your Fighter: ', [' ']+list(names)+['Random'])
pokemon2 = st.selectbox('Player 2 Choose Your Fighter: ', [' ']+list(names)+['Random'])

if pokemon1 == 'Random':
    pokemon1 = pokemon_df['name'].sample().values[0]
if pokemon2 == 'Random':
    pokemon2 = pokemon_df['name'].sample().values[0]    
if pokemon1 != ' ' and pokemon2 != ' ':
    if st.button('BATTLE!'):
        st.header(pokemon1)
        st.image(pokebot.get_pic_path(pokemon1))
        time.sleep(3)
        st.write('\nVs.\n')
        time.sleep(3)
        st.header(pokemon2)
        st.image(pokebot.get_pic_path(pokemon2))
        
        if pokemon1 == pokemon2:
            pokemon2 += ' '
        player_dict = {pokemon1:'Player 1',pokemon2:'Player 2'}
        attacker, defender = np.random.choice([pokemon1, pokemon2], 2, replace=False)
        
        hp1 = np.random.randint(50,101)
        hp2 = np.random.randint(50,101)
        hp_dict = {attacker: hp1, defender: hp2}
        while hp_dict[attacker] > 0:
            time.sleep(3)
            hit_tup = pokebot.attack(attacker, defender)
            if len(hit_tup) == 2:
                st.write(f'{attacker} uses {hit_tup[0]} and misses!')
                attacker, defender = defender, attacker
            else:
                if hit_tup[2] < 30:
                    st.write(f'{attacker} uses {hit_tup[0]} and hits! {defender} deals {hit_tup[2]} damage!')
                else:
                    st.write(f'{attacker} uses {hit_tup[0]}... CRITICAL HIT!!! {attacker} deals {hit_tup[2]} damage!')
                hp_dict[defender] -= hit_tup[2]
                attacker, defender = defender, attacker
            st.write(f'{attacker} has {max(hp_dict[attacker], 0)} hp. {defender} has {max(hp_dict[defender], 0)} hp.\n')
        st.write(f'{player_dict[defender]} ({defender}) is the victor!')
        st.image(pokebot.get_pic_path(defender))
        st.stop()
    
    

        
        
    
    

    