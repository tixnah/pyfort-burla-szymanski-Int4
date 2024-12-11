import random
def shell_game():
    L = ['A', 'B', 'C']
    attempt = 1
    key_count = 0

    while attempt <= 2 :
        guess = random.choice(L)
        user_guess = input("Choose a shell between A, B or C : ")

        if user_guess in L :
            if user_guess == guess :
                print("Correct ! You win a key !")
                key_count += 1
            else :
                print("Wrong choice, you got", 2 - attempt, "attempt left.")
        else :
            print("Wrong input.")        #Verifies if the user's input is really one of the options

        attempt += 1