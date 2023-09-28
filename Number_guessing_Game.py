#Number Guessing Game
import random
heading ="""
   _____                          _   _                                     _                 _  
  / ____|                        | | | |                                   | |               | | 
 | |  __ _   _  ___  ___ ___     | |_| |__   ___      _ __  _   _ _ __ ___ | |__   ___ _ __  | | 
 | | |_ | | | |/ _ \/ __/ __|    | __| '_ \ / _ \    | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__  | | 
 | |__| | |_| |  __/\__ \__ \    | |_| | | |  __/    | | | | |_| | | | | | | |_) |  __/ |    |_| 
  \_____|\__,_|\___||___/___/     \__|_| |_|\___|    |_| |_|\__,_|_| |_| |_|_.__/ \___|_|    (_) 
"""                                                                                               

print(heading) 

def guess_the_number(chance):
    print(f"You have {chance} chances\n")
    n = chance
    while n > 0:
        guess = int(input("\nGuess a number between 1 to 100: "))
        n -= 1
        if guess > num:
            print("Too high!\nGuess again")
        elif guess < num:
            print("Too low!\nGuess again")
        else:
            print(f"You guessed the correct number in {chance-n} trials, which is {num}!")
            break
        print(f"You are left with {n} chances:)")
    print(f"You couldn't guess the number in {chance} chances! The correct guess was {num}! You lose!!")


num = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")
print("Choose difficulty Level: Easy / Hard ")
level = input("Enter E for easy level and H for hard level: ")
if level == 'E' or level == 'e':
    guess_the_number(10)
elif level == 'H' or level == 'h':
    guess_the_number(5)
else:
    print("Invalid input!!")

