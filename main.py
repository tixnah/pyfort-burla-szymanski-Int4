#FORT BOYAR PROJECT
#Cristina Burla and Laure Szymanski

#The role of this file is to launch the game by using all the functions wa created in the game() function.

#importing all the modules

import time
from logical_challenge import *
from chance_challenges import *
from utility_function import *
from pere_fouras_challenge import *
from final_challenge import *
from math_challenges import *

###structure
# introduction
#team compo
#loop until the team has 3 keys.
#menu of challenge types, and select one
#choose of player
#launch a game randomly ( in the type range)
#if the player win the game he wins a key
#when the user have 3 keys the final challenge is unlock.


def game():
    # display the game using all the previous function and giving a winner.

    ##initialisation
    team_key_count = 0
    #empty list to store the composition of the team.
    team = []

    introduction()

    team = compose_equipe()

    #choice of the game

    while team_key_count<1:
        type_of_challenge = challenge_menu()

        player= choose_players(team)
        print()
        print("{} will be playing the game.".format(player['name']))
        print()

        result= False #initialisation of the variable

        #depending on the input of the user the game will start.
        if type_of_challenge == 1:
            result=math_challenge()
        elif type_of_challenge == 2:
            result=nim_game()
        elif type_of_challenge == 3:
            result = chance_challenge()
        elif type_of_challenge ==4:
            result=pere_fouras_riddles()

        #if the use won the game the key count of the whole team takes one more and the personal score of the player always add one.
        if result :
            team_key_count+=1
            player['key_won']+=1
            time.sleep(1)
            print("You win a key.")
            print()
            time.sleep(1)
            print("The team has overall {} keys".format(team_key_count))
            time.sleep(1)

        #if the player do not win the following message will appear.
        else :
            print("You don't win a key :(.")
            time.sleep(1)
            print()
            print("You overall have {} keys".format(team_key_count))
            time.sleep(1)

    #when escaping the loop it means you have 3 keys and you access the treasure room to do the final challenge.
    print()
    print("You are entering the treasure room! Good luck.")
    time.sleep(1)
    print()
    final_result=treasure_room()
    if final_result :
        print("You won the treasure !")

        #we want to know who won the more keys if they are more than one player:
        max_keys=-1 # -1 because the player are initialize with 0 so we will always find someone with a superior key count.
        max_player= {} #initialisation of the dictionary
        if len(team)>1:
            for player in team:
                print()
                print("Now we are designing the winner between all the contestant!")
                time.sleep(2)
                print("{} have {} key(s).".format(player['name'],player['key_won']))
                if player['key_won']>max_keys:
                    max_keys=player['key_won']#if the number of keys that the player being iterated through is superior to the initial value of 'max_keys' then 'max_keys' takes the number of keys of the player as its new value.
                    max_player=player# and the new max_player take the player that has the max number of keys.
            print("The player that has won the maximum key is {}".format(max_player['name']))
            print()
            print("Thank you for playing!")
            print("Good bye!")
        print()


        if len(team)== 1:#if there is only one member then he can be the only who has won the 3 keys.
            print()
            print("{}, thank you for playing the game!").format(team[0]['name'])
            print()
            print("Good bye!")
    else:
        time.sleep(2)
        print()
        print("You lost so you can not access the treasure, but thank you for playing the game!")
        print()
        print("Good bye!")

#starts the function/game.
game()
