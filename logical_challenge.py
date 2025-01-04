# The game of Nim
def display_sticks (n) :
    print("Remaining sticks : ", "|" * n) #displays the number of sticks remaining

def player_removal(n) :
    print("Player's turn.")
    p_choice = int(input("How many stick do you want to remove? (1, 2 or 3): "))    #the player makes his choice
    while p_choice not in [1, 2, 3] and p_choice > n :      #if the choice is invalid, he has to try again
        print("That's not a valid choice.")
        p_choice = int(input("How many stick do you want to remove? (1, 2 or 3): "))
    return (n - p_choice)       #returns the number of sticks after the choice

def master_removal(n) :
    m_choice = n % 4            #the game master makes his choice
    while m_choice == 0 or m_choice > 3 :       #if the choice is invalid, he has to try again
        m_choice = n % 4
    print("The game master removes {} sticks".format(m_choice))
    return (n - m_choice)       #returns the number of sticks after the choice

def nim_game() :
    numb_sticks = 20    #initializing to 20 stick
    p_turn = True       #player turn as a boolean
    display_sticks(numb_sticks)

    while numb_sticks > 0 :
        if p_turn :                 #if it is the player's turn
            numb_sticks = player_removal(numb_sticks)
        else :                      #if it is not the player's turn
            numb_sticks = master_removal(numb_sticks)
            display_sticks(numb_sticks)                 #will display the number of sticks after each move
        p_turn = not p_turn         #switches turns

    if p_turn :
        print("The game master removed the last stick, you win a key !")
        return True
    else :
        print("You removed the last stick, you lose :( ")
        return False