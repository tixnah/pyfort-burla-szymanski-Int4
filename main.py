#import of all the modules used

import random
from mathematique_challenges import *
from chance_challenges import *
from logical challenges import *
from pere_fouras_challenge import *
from final_challenge import *
from utility_function import *


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
    ##initialisation
    team_key_count = 0
    #empty list to store the composition of the team.
    team = []

    introduction()

    team = compose_equipe()

    #choice of the game

    while team_key_count<3:
        type_of_challenge = challenge_menu()
        challenges ={
            1:["math_roulette_challenge","math_challenge_prime","math_challenge_equation",],
            2:["Logical_challenge"],
            3:["Chance_challenge1","Chance_challenge2","Chance_challenge3"],
            4:["père_Fouras_Riddle"]
        }
        random_challenge= random.choice(challenges[type_of_challenge])

        print("You will be playing : {}".format(random_challenge))

        result_of_challenge=random_challenge() #execution of the function

        player=choose_players(team)
        #choose a random game in the challenge type the player choosed.
        if result_of_challenge=True :
            team_key_count+=1
            team[player-1][key_count]+=1
            print("Correct! You win a key.")
            print("You have overall {} keys".format(team_key_count))

        else :
            print("You lost :( and don't win a key!")
            print("You have overall {} keys".format(team_key_count))

    #when escaping the loop it means you have 3 keys and you acces the treasure room to do the final challenge.
    final_challenge()









