#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:48:00 2019

@author: flatironschool
"""

game_dictionary = {'home': {'team_name': 'Brooklyn Nets', 
                            'colors': ['Black', 'White'], 
                            'players':{'Alan Andersen': {'Number': 0,
                                                       'Shoe' : 16, 
                                                       'Points': 22, 
                                                       'Rebounds': 12, 
                                                       'Assists': 12, 
                                                       'Steals': 3, 
                                                       'Blocks': 1, 
                                                       'slam dunks': 1},
                                    'Reggie Evans':{'Number': 30, 
                                                    'Shoe': 14,
                                                    'Points': 12,
                                                    'Rebounds': 12,
                                                    'Assists': 12,
                                                    'Steals': 12,
                                                    'Blocks': 12,
                                                    'slam dunks': 7},
                                    'Brook Lopez':{'Number': 11,
                                                   'Shoe': 17,
                                                   'Points': 17,
                                                   'Rebounds': 19,
                                                   'Assists': 10,
                                                   'Steals': 3,
                                                   'Blocks': 1,
                                                   'slam dunks': 15},
                                    'Mason Plumley':{'Number': 1,
                                                     'Shoe': 19,
                                                     'Points': 26,
                                                     'Rebounds': 12,
                                                     'Assists': 6,
                                                     'Steals': 3,
                                                     'Blocks':8,
                                                     'slam dunks': 5},
                                    'Jason Terry':{'Number': 31,
                                                   'Shoe': 15,
                                                   'Points': 19,
                                                   'Rebounds': 2,
                                                   'Assists': 2,
                                                   'Steals': 4,
                                                   'Blocks': 11,
                                                   'slam dunks': 1}}},
                    'away':{'team_name': 'Charlotte Hornets', 
                            'colors': ['Turquoise', 'Purple'], 
                            'players':{'Jeff Adrien': {'Number': 4,
                                                       'Shoe' : 18, 
                                                       'Points': 10, 
                                                       'Rebounds': 1, 
                                                       'Assists': 1, 
                                                       'Steals': 2, 
                                                       'Blocks': 7, 
                                                       'slam dunks': 2},
                                    'Bismack Biyombo':{'Number': 0, 
                                                    'Shoe': 16,
                                                    'Points': 12,
                                                    'Rebounds': 4,
                                                    'Assists': 7,
                                                    'Steals': 7,
                                                    'Blocks': 15,
                                                    'slam dunks': 10},
                                    'Dasagna Diop':{'Number': 2,
                                                   'Shoe': 14,
                                                   'Points': 24,
                                                   'Rebounds': 12,
                                                   'Assists': 12,
                                                   'Steals': 4,
                                                   'Blocks': 5,
                                                   'slam dunks': 5},
                                    'Ben Gordon':{'Number': 8,
                                                     'Shoe': 15,
                                                     'Points': 33,
                                                     'Rebounds': 3,
                                                     'Assists': 2,
                                                     'Steals': 1,
                                                     'Blocks': 1,
                                                     'slam dunks': 0},
                                    'Brendan Haywood':{'Number': 33,
                                                   'Shoe': 15,
                                                   'Points': 6,
                                                   'Rebounds': 12,
                                                   'Assists': 12,
                                                   'Steals': 22,
                                                   'Blocks': 5,
                                                   'slam dunks': 12}}}}
                                    
#def good_practices():
  #for location, team_stats in game_dict().items():
    # are you ABSOLUTELY SURE what 'location' and 'team_stats' are? use pdb.set_trace() to find out!
    #import pdb; pdb.set_trace()
      #for stats, data in team_stats.items():
        # are you ABSOLUTELY SURE what 'stats' and 'data' are? use pdb.set_trace() to find out!
        #import pdb; pdb.set_trace()
        # what is 'data' at each level of the for loop block? when will we be able to iterate through a list? 
        # When would the following line of code break?
       # for item in data:
            #print(item)