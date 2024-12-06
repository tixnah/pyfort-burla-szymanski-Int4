import random
from chance_challenges import *

# implementation of the shell game
print("Welcome to the shell game !")
print("You must guess which of the three shells (A, B, or C) hides the key. You have two attempts to find it. On each attempt, the key is randomly placed under one of the shells.")
print("Good luck ;)")
L = ['A', 'B', 'C']
key_count = 0
guess = False
attempt = 1
for attempt in range(2):
    to_guess = random.choice(L)
    user_guess = input("Choose a shell between A, B and C : ")
    attempt += 1
    if shell_game(to_guess, user_guess):
        print("Correct ! You win a key !")
        key_count += 1
    else:
        print("Wrong choice, you got", 2 - attempt, "attempts left :(")

# implementation of the rolling dice game
