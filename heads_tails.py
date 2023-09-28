# Heads or Tails
import random	 

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
coin_face = random.randint(0, 1)
if coin_face == 1:
    print("Heads")
else:
    print("Tails")


import random 

# generate random integer from 1 to 10
random_integer = random.randint(1, 10)
print(random_integer)

# generate random number between 0 to 1
random_float = random.random()   
print(random_float)

# generate random number between 0 to 5
random_number = random.random() * 5
print(random_number)