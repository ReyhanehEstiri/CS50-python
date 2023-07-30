def main():
    coins()


def coins():
    amount_due = 50
    accepted_coins = [25, 10, 5]

    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        input_coin = int(input("Insert Coin: "))
        if input_coin in accepted_coins:
            amount_due -= input_coin
        if amount_due <= 0:
            print(f"Change Owed: {amount_due * -1}")


if __name__ == "__main__":
    main()
