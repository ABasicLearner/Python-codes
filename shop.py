items = ['book', 'pen', 'pencil', 'sharpner']
stock = [10, 12, 15, 20]
price = [50, 10, 7, 5]
cost_price = [40, 7, 5, 2]
choice = 'yes'
amount = sell = cp = 0
while choice == 'yes':
    idx = 0
    for i, s, p in zip(items, stock, price):
        idx += 1 
        print(idx, i, s, p)
    idx = 0
    order = int(input("What do you want to buy: "))
    qty = int(input("How much quantity you want: "))
    amount = amount + (qty*price[order-1])
    stock[order-1] = stock[order-1] - qty
    sell = sell + (price[order-1] * stock[order-1])
    cp = cp + (cost_price[order-1] * stock[order-1])
    for i, s, p in zip(items, stock, price):
        idx += 1
        print(idx, i, s, p)
    choice = input("Do you want to continue, yes/no: ")

print(f"Total sell of Rs.{sell}")
print(f"Total profit on the sold items is Rs.{cp}")



    