#RPG v1.0
#Patzy 3/25/2022

import cmd
import textwrap
import time
import os
import random
import sys

screen_width = 100

##### Player Setup #####
class player:
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = 'start'
myPlayer = player()

##### Title Screen #####
def title_screen():
    os.system('clear')
    print("#######################")
    print("#  Welcome to my RPG  #")
    print("#######################")
    print("# Coded by Patzy 2022 #")
    print("#######################")
    print("#      New Game       #")
    print("#      Load Game      #")
    print("#       Options       #")
    print("#        Help         #")
    print("#        Quit         #")
    print("#######################")
    print(">> Please select and option: ")
    title_screen_selection()


##### Title Screen Selection ######
def title_screen_selection():
    print("Please select and option: ")
    option = input(">> ")
    if option.lower == ("new", "new Game"):
        new_game(new) ## Placeholder
    elif option.lower == ("load", "load Game", "play", "resume"):
        load_game() ## Placeholder
    elif option.lower == ("option", "options"):
        option_menu()
    elif option.lower == ("help" , "?"):
        help_menu()
    elif option.lower == ("quit", "stop", "done", "exit"):
        sys.exit()
    else:
        print("Please select a valid option: ")
        
def help_menu():
    print("Use up, down, left, right to move. ")
    print("Type your commands to take an action.")
    print("Use look to examine an object. ")


# #### Game Functionality #####
def start_game()



##### MAP ######
# a1, a2 ...     a6
#-------------------
#|  |  |  |  |  |  |  a6
#-------------------
#|  |  |  |  |  |  |  b6
#-------------------
#|  |  |  |  |  |  |  ...
#-------------------
#|  |  |  |  |  |  |
#-------------------
#|  |  |  |  |  |  |
#-------------------
#|  |  |  |  |  |  |  f6
#-------------------

ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up', 'north'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'
DOWN = 'down', 'south'

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False, 'a5': False, 'a6': False,
                    'b1': False, 'b2': False, 'b3': False, 'b4': False, 'b5': False, 'b6': False,
                    'c1': False, 'c2': False, 'c3': False, 'c4': False, 'c5': False, 'c6': False,
                    'd1': False, 'd2': False, 'd3': False, 'd4': False, 'd5': False, 'd6': False,
                    'e1': False, 'e2': False, 'e3': False, 'e4': False, 'e5': False, 'e6': False,
                    'f1': False, 'f2': False, 'f3': False, 'f4': False, 'f5': False, 'f6': False,
}

zonemap = {
        'a1': {
            ZONENAME: "",
            DESCRIPTION = 'description'
            EXAMINATION = 'examine'
            SOLVED = False
            UP = ''
            LEFT = ''
            RIGHT = 'a2'
            DOWN = 'b1'
            
        } ### Complete the rest of the map zones and fill in Description and Examination
        }

##### Game Interactivity ######
def print_location();
    print ('\n' + '#' * (4 + len(myPlayer.location)))
    print ('#' + myPlayer.location.upper() + '#')
    print ('#' + zonemap[myPlayer.location][DESCRIPTION] + '#')
    print ('\n' + '#' * (4 + len(myPlayer.location)))

def prompt():
    print("\n" + "================================")
    print("What would you like to do? ")
    action = input(">> ")
    acceptable_actions = ['move', 'travel', 'go', 'walk', 'run', 'examine', 'inspect', 'interact', 'look', 'fight']
    while action.lower() not in acceptable_actions:
        print("Uknown action. Please Try Again.\n")
        action = input(">> ")
    if action.lower() == 'quit': 
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk', 'run']:
        player_move(action.lower())
    elif action.lower() in ['examine', 'inspect', 'interact', 'look'
        player_examine(action.lower())
    else action.lower() == "fight":
        player_fight(action.lower()

def player_move(action):
    
        ask 