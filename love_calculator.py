print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is his/her name? \n")
name = name1 + name2
name = name.lower()
n1 = 0
n2 = 0
for i in 'true':
    n1 = n1 + name.count(i)
for j in 'love':
    n2 = n2 + name.count(j)
result = str(n1) + str(n2)
r = int(result)
if r<10 or r>90:
    print(f"Your score is {r}, you go together like coke and mentos.")
elif r>=40 and r<=50:
    print(f"Your score is {r}, you are alright together.")
else:
    print(f"your score is {r}.")

#alternate code

print()
print("Welcome to the Love Calculator!")
name1 = input("Enter your name:  ")
name2 = input("Enter his/her name:  ")
name1 = name1.lower()
name2 = name2.lower()
count1 = 0
count2 = 0
for i in name1:
    if i == 't' or i == 'r' or i == 'u' or i == 'e':
        count1 = count1 + 1
    if i == 'l' or i == 'o' or i == 'v' or i == 'e':
        count2 = count2 + 1

for i in name2:
    if i == 't' or i == 'r' or i == 'u' or i == 'e':
        count1 = count1 + 1
    if i == 'l' or i == 'o' or i == 'v' or i == 'e':
        count2 = count2 + 1 
        
result = str(count1) + str(count2)
r = int(result)
print()
if r<10 or r>90:
    print(f"Your score is {r}, you go together like coke and mentos.")
elif r>=40 and r<=50:
    print(f"Your score is {r}, you are alright together.")
else:
    print(f"your score is {r}.")


#one more solution

"""
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = name1.lower()
name2 = name2.lower()
n1 = 0
n2 = 0
n3 = 0
n4 = 0
for i in 'true':
    n1 = n1 + name1.count(i)
    n2 = n2 + name2.count(i)
for j in 'love':
    n3 = n3 + name1.count(j)
    n4 = n4 + name2.count(j)
c1 = n1+n2 
c2 = n3+n4
result = str(c1) + str(c2)
r = int(result)
if r<10 or r>90:
    print(f"Your score is {r}, you go together like coke and mentos.")
elif r>=40 and r<=50:
    print(f"Your score is {r}, you are alright together.")
else:
    print(f"your score is {r}.")
"""

