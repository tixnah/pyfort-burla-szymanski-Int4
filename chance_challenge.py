import random

#shell game function
def shell_game():
    l = ['A', 'B', 'C']     #initialization of the list of shells
    attempt = 1             #initialization of the number of attempts
    found = False

    while found == False and attempt <= 2 :   #the loop is working while the shell is not found and the maximum number of attempt is not reached
        guess = random.choice(l)              #the program randomly chooses the shell
        user_guess = input("Choose a shell between A, B or C : ") #the user chooses the shell they want

        while user_guess != 'A' and user_guess != 'B' and user_guess != 'C' :  #the player has to choose a shell as long as the input is not one of the letters expected
            print("Invalid choice")
            user_guess = input("Choose a shell between A, B or C : ")

        if user_guess in l :            #to make sure the user's input is one of the elements in the list
            if user_guess == guess :    #verifies if the user input is the same as the program choice
                print("Correct ! You win a key !")
                found = True
            elif user_guess != guess and attempt < 2 :  #the player made a wrong choice so he got to play again
                print("Wrong choice, you got {} attempt left.".format(2-attempt))
                found = False
            elif user_guess != guess and attempt == 2:  #if the player did not find the shell on his second and last attempt, he loses
                print("You lose... The key was under shell {} :(".format(guess))
                found = False
        attempt += 1    #the number of attempt increases by 1 on each try


# Rolling dice game function
def roll_dice_game():
    max_attempts = 3

    for attempt in range(1, max_attempts + 1):      #the game will play until 3 attempts
        print("This is your attempt number {}.".format(attempt))    #tells the player in which attempt he plays
        input("Roll the dice by pressing the *Enter* key.")         #the player rolls his dice
        player_dice = (random.randint(1, 6), random.randint(1, 6))  #the program chooses the values of the player's dice
        print("You obtained {}.".format(player_dice))       #displays the values obtained by the player

        if 6 in player_dice :       #if the player has a 6, he wins and the challenge stops
            print("You won! Here is a key")
            return True

        print("This is now the game master's turn")
        master_dice = (random.randint(1, 6), random.randint(1, 6))  #the program chooses the values of the master's dice
        print("The game master obtained {}.".format(master_dice))               #displays the values obtained by the master

        if 6 in master_dice :        #if the master has a 6, he wins and the challenge stops
            print("The game master got a 6, you lose :(")
            return False

        print("No one rolled a 6 on this round, let's try again")   #if no one had a 6 during the attempt, another attempt starts

    print("No one scored a 6, that's a draw.")       #if no one had a 6 in the 3 attempts, the challenge stops
    return False

def chance_challenge() :
    challenge = random.choice(["A", "B"])
    key = 0

    if challenge == "A" :

        # implementation of the shell game
        print("Welcome to the shell game !")
        print("You must guess which of the three shells (A, B, or C) hides the key. You have two attempts to find it. On each attempt, the key is randomly placed under one of the shells.")
        print("Good luck ;)")
        shell_game()

    elif challenge == "B" :

        # implementation of the rolling dice game
        print("Welcome to the rolling dice game !")
        print("You play against the Game Master. The first to roll a 6 wins ! You have 3 attempts to try to win.")
        print("Good luck ;)")
        roll_dice_game()