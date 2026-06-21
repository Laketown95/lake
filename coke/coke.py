# Price display
price = 50
total_paid = 0
coins = [25, 10, 5]

#while loop
while price > 0:
    #f string evaluate expression inside of string {}
    print(f"Amount Due: {price}")
    #input int
    pay = int(input("Insert Coin: "))
    if pay in coins:
        # Update price and total_paid for every valid transcation
        price = price - pay
        total_paid = total_paid + pay
if total_paid >= price:
    print(f"Change Owed: {total_paid - 50}")
