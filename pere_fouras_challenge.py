#FORT BOYAR PROJECT
#Cristina Burla and Laure Szymanski

#The role of this file is to store the pere fouras challenge.

import json
import random
import time

def load_riddles(file): #take as parameter a json file.
    #  take riddles from the JSON file.
    with open(file, 'r',encoding='utf-8') as f:
        riddles = json.load(f)
    return riddles


def pere_fouras_riddles():

    #Returns True if the player wins, False if he doesnt.
    # Local variables
    riddles_list = load_riddles("PFRiddles.json")  # Load riddles from the fil
    selected_riddle = random.choice(riddles_list)  # Randomly select a riddle
    attempts = 3 #number of attemps

    print("Welcome to the père fouras' challenge!")
    print("The Pere Fouras's Riddle is :")
    print(selected_riddle['question'])  # print the riddle

    #  loop for tries
    while attempts > 0:
        player_answer = input("Your answer: ")  # ask player's answer
        if player_answer.lower().strip() == selected_riddle['answer'].lower().strip() :  # is the answer correct? and the ".lower().strip()" is used to meke it not case sensitive and ignores extra spaces in the input.
            time.sleep(1)
            print("Correct! You win a key!")
            time.sleep(4)
            return True  # the player win a key
        else:
            # Decrease attempts for each wrong answer until zero attempts left.
            attempts -= 1
            if attempts > 0:
                time.sleep(1)
                print("Your answer is incorrect! You have {} attempt(s) remaining.".format(attempts))
            else:
                time.sleep(4)
                print("Sorry, you don't have any tries left !")
                time.sleep(1)
                print("The correct answer was: {}".format(selected_riddle['answer']))
                return False  # Player doesnt win

