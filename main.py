#init of key_count
key_count=0
print("You have {} keys".format(key_count))

from mathematique_chal import *

if math_challenge_prime():
    print("Correct! You win a key.")
    key_count+=1
else:
    print("do better next time, you've just lost an opportunity to win a key!")
print("You have {} keys".format(key_count))

from mathematique_chal import *
if math_roulette_challenge():
    print("Correct! You win a key.")
    key_count+=1
else:
    print("You lost the opportunity to win a key!")

print("You have {} keys".format(key_count))

