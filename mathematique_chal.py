#prime numbers challenge

def is_prime(n):
    if n == 1:
        return False
    for i in range(2,n):
        if n%i==0 and i!=n:
            return False
        else:
            return True
#comment
def nearest_prime(n):
    prime_list = []
    for i in range(n+1,2*n):
        if is_prime(i):
            prime_list.append(i)        # we are adding al the prime number from 2 to 2n and adding it to a list.
    return prime_list[0]

    # we are looking for the value with the minimum difference from n, and attributing it to a variable.


import random
def math_challenge_prime():
    n=random.randint(10,20)
    players_answer=int(input("find the prime number closer to {}".format(n)))
    print(nearest_prime(n))
    if nearest_prime(n)==players_answer:
        return True
    else:
        return False

#math Roulette challenge
def math_roulette_challenge():
    random_list=[]
    for i in range (5):
        random_list.append(random.randint(1,20))
    print("Numbers on the roulette are:")
    print(random_list)
    operator=random.choice(['addition','subtraction','multiplication'])
    print("Calculate the result by combining these numbers with {}".format(operator))
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

    if players_answer==val:
        return True
    else:
        return False

#linear equation
 def solve_linear_equation():
     a=random.randint(1,10)
     b=random.randint(1,10)
     return -b/a
 def math_challenge_equation():





