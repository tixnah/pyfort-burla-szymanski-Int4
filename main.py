#import of all the modules used

#from chance_challenges import *
#from logical_challenges import *
#from final_challenge import *

import random
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
        challenges ={
            1:["math_roulette_challenge","math_challenge_prime","math_challenge_equation",],
            2:["Logical_challenge"],
            3:["Chance_challenge1","Chance_challenge2","Chance_challenge3"],
            4:["pere_fouras_riddles"]
        }
        random_challenge= random.choice(challenges[type_of_challenge])
        player,index_player = choose_players(team)
        print("{} will be playing".format(player['name']))
        print("You will be playing : {}".format(random_challenge))

        random_challenge= globals()[random_challenge] # we use global to get the actual function reference and not just its name

        result =random_challenge()

        #choose a random game in the challenge type the player choosed.
        if result :
            team_key_count+=1
            team[index_player-1]['key_won']+=1
            print("You win a key.")
            print("You have overall {} keys".format(team_key_count))

        else :
            print("You don't win a key :(.")
            print("You overall have {} keys".format(team_key_count))

    #when escaping the loop it means you have 3 keys and you access the treasure room to do the final challenge.
    #final_challenge()

game()







