from chance_challenges import *
from logical_challenges import tictactoe_game

key_count = 0  # to count the number of keys in the game

# implementation of the shell game
print("Welcome to the shell game !")
print("You must guess which of the three shells (A, B, or C) hides the key. You have two attempts to find it. On each attempt, the key is randomly placed under one of the shells.")
print("Good luck ;)")
if shell_game() :
    key_count += 1  # the player wins a key


# implementation of the rolling dice game
print("Welcome to the rolling dice game !")
print("You play against the Game Master. The first to roll a 6 wins ! You have 3 attempts to try to win.")
print("Good luck ;)")
if roll_dice_game() :
    key_count += 1  # the player wins a key

if tictactoe_game() :
    key_count += 1