"""
You are playing a card game, where 'n' cards of different colours arranged in a list on a circular table. 
The player must move one card at a time, either to left or right. Since the cards are in a circular list, 
when last card is reached in either direction, the next card is at the other end of the list.
You are given with one card color and one card index, determine the minimum number of left or right moves to 
reach the given target card from the given start index.
1<=n<=100
0<=startindex<=n-1
1<=cards[i] and targetCard<=100
"""
def card(n, cards, num, color):
    moves = 0
    i = num
    while 1:
        if cards[i] == color:
            return moves
            break
        i = (i+1) % n
        moves += 1
    return -1

numOfCards = input("\nEnter number of colors: ")
n = int(numOfCards)
cards = []
print("\nEnter card colors: ")
for i in range(n):
    cards.append(input("Enter color: "))
print("The list of card colors is: ",cards)
num = int(input("\nEnter the startindex(consider elements starting with index 0):  "))
color = input("\nEnter the target color:  ")
print('\n',color, "is found after", card(n, cards, num, color), "moves")

