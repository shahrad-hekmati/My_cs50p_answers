amount_due = 50
print(f"Amount Due: {amount_due}")
add_coin = 0

while True:

    coin = int(input("Insert Coin: "))

    if coin == 25:
        amount_due -= 25
        print(f"Amount Due: {amount_due}")
        add_coin += 25

    elif coin == 10:
        amount_due -= 10
        print(f"Amount Due: {amount_due}")
        add_coin += 10

    elif coin == 5:
        amount_due -= 5
        print(f"Amount Due: {amount_due}")
        add_coin += 5

    else:
        print(f"Amount Due: {amount_due}")

    if add_coin >= 50:
        print(f"Change Owed: {add_coin - 50}")
        break

    else:
        print(f"Amount Due: {amount_due}")