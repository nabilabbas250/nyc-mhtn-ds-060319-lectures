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

#print(home_team_name())

def good_practices():
  for location, team_stats in game_dictionary.items():
    # are you ABSOLUTELY SURE what 'location' and 'team_stats' are? use pdb.set_trace() to find out!
    import pdb; pdb.set_trace()
      for stats, data in team_stats.items():
        # are you ABSOLUTELY SURE what 'stats' and 'data' are? use pdb.set_trace() to find out!
        import pdb; pdb.set_trace()
        # what is 'data' at each level of the for loop block? when will we be able to iterate through a list? 
        # When would the following line of code break?
        for item in data:
            print(item)