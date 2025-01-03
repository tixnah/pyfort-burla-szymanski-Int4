#import of all the modules used


#from logical_challenges import *
#from final_challenge import *

import random
from chance_challenges import *
from utility_function import *
from pere_fouras_challenge import *

from mathematique_challenges import *

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

        player= choose_players(team)

        print("{} will be playing the game".format(player['name']))

        result= None

        if type_of_challenge == 1:
            result=math_challenge()
        elif type_of_challenge == 2:
            result=logical_challenge()
        elif type_of_challenge == 3:
            result = chance_challenge()
        elif type_of_challenge ==4:
            result=pere_fouras_riddles()

        if result :
            team_key_count+=1
            #team[index_player-1]['key_won']+=1
            print("You win a key.")
            print("You have overall {} keys".format(team_key_count))

        else :
            print("You don't win a key :(.")
            print("You overall have {} keys".format(team_key_count))

    #when escaping the loop it means you have 3 keys and you access the treasure room to do the final challenge.
    #final_challenge()

game()







