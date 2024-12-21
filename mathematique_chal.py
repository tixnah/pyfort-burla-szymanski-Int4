#prime numbers challenge

def is_prime(n):
    #return true if the number is prime
    if n == 1:
        return False
    for i in range(2,n):
        if n%i==0 and i!=n:
            return False
        else:
            return True
#comment
def nearest_prime(n):
    #returns the closest prime from the number n
    prime_list = []
    for i in range(n+1,2*n):
        if is_prime(i):
            prime_list.append(i)        # we are adding all the prime number from 2 to 2n and adding it to a list.
    return prime_list[0]

    # we are looking for the value with the minimum difference from n, and attributing it to a variable.


import random
def math_challenge_prime():

    #return true if the player has the good answer

    n=random.randint(10,20)
    players_answer=int(input("find the prime number closer to {}".format(n)))
    print(nearest_prime(n))

    if nearest_prime(n)==players_answer: #check if the input of the player is good
        return True
    else:
        return False

#math Roulette challenge
def math_roulette_challenge():
    # local variable
    random_list=[]

    for i in range (5):
        random_list.append(random.randint(1,20)) #adding to the list 5 random numbers between 1 and 20.

    #display the numbers
    print("Numbers on the roulette are:")
    print(random_list)

    operator=random.choice(['addition','subtraction','multiplication']) #random choice of an operator

    print("Calculate the result by combining these numbers with {}".format(operator)) #display the operator

    players_answer=int(input("Your answer:"))

    if operator=='addition':
        sum(random_list)
    if operator=='subtraction':
        val = random_list[0]
        for num in random_list[1:]:
            val -= num
    if operator=='multiplication':
        val=1
        for num in random_list:
            val*=num

    if players_answer==val:#check if the answer of the player is right
        return True
    else:
        return False

#linear equation
 def solve_linear_equation():
     a = random.randint(1, 10)
     b = random.randint(1, 10)
     return a,b,-b/a

 def math_challenge_equation():
    a,b,solution=solve_linear_equation() # the value a, b and solution are the output of the function "solve_linear_equation".

    print("Solve the equation {}x + {} = 0.".format(a,b))
    player_answer = float(input("What is the value of x: "))
     if player_answer == solution: #check if the answer of the player is the same as the solution.
         return True
     else:
         return False







