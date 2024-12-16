import random
def shell_game():
    L = ['A', 'B', 'C']
    attempt = 1
    key_count = 0
    found = False

    while found == False and attempt <= 2 :
        guess = random.choice(L)
        user_guess = input("Choose a shell between A, B or C : ")

        while user_guess != 'A' and user_guess != 'B' and user_guess != 'C' :
            user_guess = input("Choose a shell between A, B or C : ")

        if user_guess in L :
            if user_guess == guess :
                print("Correct ! You win a key !")
                key_count += 1
                found = True
            elif user_guess != guess and attempt < 2 :
                print("Wrong choice, you got", 2 - attempt, "attempt left.")
                found = False
            elif user_guess != guess and attempt == 2:
                print("You lose...")
                found = False
        attempt += 1

