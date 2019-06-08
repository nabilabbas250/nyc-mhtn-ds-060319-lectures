#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:45:04 2019

@author: flatironschool
"""

#Make a bunch of functions to operate on out new dictionary.
from Lab_NBA import *

#def home_team_name():
    #return game_dictionary['home']['team_name']

#print(home_tea.m_name())

#def num_points_scored:
    #input = player, output = points
#print(game_dictionary['home']['players']['Reggie Evans']['Points'])


def team_colors(Team_Name):
    if game_dictionary['home']['team_name'] == Team_Name:
        return game_dictionary['home']['colors']
    else :
        return game_dictionary['away']['colors']
    
#print(team_colors('Brooklyn Nets'))
#print(team_colors('Charlotte Hornets'))
    
def team_names():
    teams = []
    teams.append(game_dictionary['home']['team_name'])
    teams.append(game_dictionary['away']['team_name'])
    return teams

#print(team_names())
    
def player_numbers(Team_Name):
    Home_Numbers = []
    Away_Numbers = []
    if game_dictionary['home']['team_name'] == Team_Name:
        for player_name in game_dictionary['home']['players'].values():
            Home_Numbers.append(game_dictionary['home']['players'][player_name]['Number'].values)
            print(player_name)
        Home_Numbers.append(game_dictionary['home']['team_name']['players'].keys())
        list(game_dictionary['home']['team_name']['players'][i]['number'])
        return
print(game_dictionary['home']['team_name']['players'].keys())

#MAKE A list of dictionaries