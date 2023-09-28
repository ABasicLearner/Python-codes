import random
import os
 
logo = """
    __  ___       __                 __                               ______                   
   / / / (_)___ _/ /_  ___  _____   / /   ____ _      _____  _____   / ____/___ _____ ___  ___ 
  / /_/ / / __ `/ __ \/ _ \/ ___/  / /   / __ \ | /| / / _ \/ ___/  / / __/ __ `/ __ `__ \/ _ 
 / __  / / /_/ / / / /  __/ /     / /___/ /_/ / |/ |/ /  __/ /     / /_/ / /_/ / / / / / /  __/
/_/ /_/_/\__, /_/ /_/\___/_/     /_____/\____/|__/|__/\___/_/      \____/\__,_/_/ /_/ /_/\___/ 
        /____/                                                                                 

"""
data = [
    {
    'Name': "Prajakta Koli",
    'Instagram Followers': 6900000,
    'Description' : "Content creator and Actress"
    },

    {
    'Name': "Rohit Saraf",
    'Instagram Followers': 2400000,
    'Description' : "Actor"
    },

    {
    'Name': "Salman Khan",
    'Instagram Followers': 55400000,
    'Description' : "Actor"
    },

    {
    'Name': "Shah Rukh Khan",
    'Instagram Followers': 32400000,
    'Description' : "Actor"
    },

    {
    'Name': "Katrina Kaif",
    'Instagram Followers': 68500000,
    'Description' : "Actress"
    },

    {
    'Name': "Vicky Kaushal",
    'Instagram Followers': 14400000,
    'Description' : "Actor"
    },

    {
    'Name': "Kapil Sharma",
    'Instagram Followers': 43600000,
    'Description' : "Comedian and Actor"
    },

    {
    'Name': "Carry Minati",
    'Instagram Followers': 16400000,
    'Description' : "Content creator"
    },

    {
    'Name': "Alia Bhatt",
    'Instagram Followers': 72600000,
    'Description' : "Actress"
    },

    {
    'Name': "Nora Fatehi",
    'Instagram Followers': 43200000,
    'Description' : "Dancer & Actress"
    },

    {
    'Name': "Guru Randhava",
    'Instagram Followers': 33300000,
    'Description' : "Singer"
    }
]


def choose_celeb():
    acc = random.choice(data)
    return acc


def Game():
    acc1 = choose_celeb()
    acc2 = choose_celeb()
    
    while 1:
        while acc1 == acc2:
            acc2 = choose_celeb()
        name1 = acc1["Name"]
        prof1 = acc1["Description"]
        fol1 = acc1["Instagram Followers"] 
        name2 = acc2["Name"]
        prof2 = acc2["Description"]
        fol2 = acc2["Instagram Followers"]
        print(f"\n1)Name: {name1}\nProfession: {prof1}\n")
        print("Vs")
        print(f"\n2)Name: {name2}\nProfession: {prof2}")
        choice = int(input("\nWhich celebrity has more followers? 1 or 2?:  "))
        if choice == 1 and fol1 >= fol2:
            os.system('cls')
            print("Correct!\n")
            print(f"Name: {name1}                   Name: {name2}")
            print(f"Ig Followers: {fol1}            Ig Followers: {fol2}")
            acc1 = acc2
            acc2 = choose_celeb()
        elif choice == 2 and fol1 <= fol2:
            os.system('cls')
            print("Correct!\n")
            print(f"Name: {name1}                   Name: {name2}")
            print(f"Ig Followers: {fol1}            Ig Followers: {fol2}")
            acc1 = acc2
            acc2 = choose_celeb()
        else:
            print("Wrong!")
            print("Game Over")
            break

            

print(logo)
print("Welcome to the Higher Lower Game!")
Game()
