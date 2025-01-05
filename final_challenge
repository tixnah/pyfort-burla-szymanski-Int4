#FORT BOYAR PROJECT
#Cristina Burla and Laure Szymanski

#The role of this file is to store the final challenge.

import json
import random


def treasure_room() :
    # Returns True if the player wins, False if he doesnt.

    with open("TRClues.json", "r") as file:     #loads the data from the file
        tv_game = json.load(file)

    years = list(tv_game["Fort Boyard"].keys())
    year = random.choice(years)                             #randomly selects a year
    shows = list(tv_game["Fort Boyard"][year].keys())
    show = random.choice(shows)                             #randomly selects a show

    clues = tv_game["Fort Boyard"][year][show]["Clues"]             #extracts clues
    code_word = tv_game["Fort Boyard"][year][show]["CODE-WORD"]     #extract code word

    print("Your clues :")
    for i in range(3) :
        print("Clue{} : {}".format(i+1, clues[i]))          #displays the first 3 clues

    attempts = 3         #initializing the number of attempts

    while attempts > 0 :
        print("You have {} attempts left".format(attempts)) #displays the number of attempts
        guess = input("Enter your guess: ").strip().upper() #the player inputs his answer

        if guess == code_word :      #if the code word is guessed
            print("Hurray, you guessed the correct answer! : {}".format(code_word)) #The player won
            return True
        else :          #if the guess is false
            attempts -= 1   #decreasing the number of attempts
            if attempts > 0 and 3 - attempts < len(clues) :       #if the player still has attempts left
                print("Incorrect answer, here is another clue :", "Clue{} : {}".format(6 - attempts, clues[5 - attempts])) #displays a new clue

    print("No more attempts :( The correct answer was {}".format(code_word))       #the player lost
    return False
