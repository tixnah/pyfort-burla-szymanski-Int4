


import json
import random


def load_riddles(file):
    #  take riddles from the JSON file.
    with open(file, 'r') as f:
        riddles = json.load(f)
    return riddles


def pere_fouras_riddles():

    #Returns True if the player wins , False if he doesnt.
    # Local variables
    riddles_list = load_riddles('riddles.json')  # Load riddles from the fil
    selected_riddle = random.choice(riddles_list)  # Randomly select a riddle
    attempts = 3

    # print the riddle
    print("Pere Fouras's Riddle:")
    print(selected_riddle['question'])

    #  loop for tries
    while attempts > 0:
        player_answer = input("Your answer: ")  # ask player's answer

        if player_answer == selected_riddle['answer']:  # is the answer correct?
            print("Correct! You win a key!")
            return True  # the player win a key
        else:
            # Decrease attempts for each wrong answer until zero attempts left.
            attempts -= 1
            if attempts > 0:
                print("Your answer is incorrect! You have {} attempt(s) remaining.".format(attempts))
            else:
                print("Sorry, you don't have any tries left !")
                print("The correct answer was: {}".format(selected_riddle['answer']))
                return False  # Player doesnt win



