#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 14:21:58 2019

@author: flatironschool
"""

def num_points_scored(name):
    if name in game_dictionary['home']['players'].keys():
        return game_dictionary['home']['players'][name]['points']
    elif name in game_dictionary['away']['players'].keys():
        return game_dictionary['away']['players'][name]['points']
    return num_points_scored
#print(num_points_scored('Ben Gordon'))


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
    if Team_Name == game_dictionary['home']['team_name']:
        for team in game_dictionary.values():
            for player in team['players'].keys():
                Home_Numbers.append(team['players'][player]['number'])
                print(Home_Numbers)
                
    elif Team_Name == game_dictionary['away']['team_name']:
        for team in game_dictionary.values():
            for player in team['players'].keys():
                Away_Numbers.append(team['players'][player]['number'])
                print(Away_Numbers)

                
#print(player_numbers('Brooklyn Nets'))

def player_stats(player_name):
    if player_name in game_dictionary['home']['players'].keys():
        return game_dictionary['home']['players'][player_name]
    elif player_name in game_dictionary['away']['players'].keys():
        return game_dictionary['away']['players'][player_name]
    return player_stats