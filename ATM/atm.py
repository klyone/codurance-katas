#!/usr/bin/env python3

class ATM:
    def __init__(self):
        pass

    def is_bill(bill_coin):
        if bill_coin > 2:
            return True
        else:
            return False

    def get_money_type(money, amount):
        money_type = "bill"

        if not ATM.is_bill(money):
            money_type = "coin"

        if amount > 1:
            money_type = money_type + "s"

        return money_type


    def count_bill_or_coin_for(bill_coin, money):
        count = 0

        for m in money:
            if m == bill_coin:
                count = count + 1

        return count


    def find_largest_bill_or_coin_for(amount):
        allowed_money = [500, 200, 100, 50, 20, 10, 5, 2, 1]

        for money in allowed_money:
            if amount >= money:
                break

        return money


    def withdraw(self, amount):
        withdraw_money = []

        while amount > 0:
            money = ATM.find_largest_bill_or_coin_for(amount)
            amount = amount - money
            withdraw_money.append(money)

        return withdraw_money

    def print_withdraw(self, amount):
        withdraw_money = self.withdraw(amount)
        previous_money = -1
        withdraw_string = ""

        for money in withdraw_money:
            if previous_money == money:
                continue

            quantity = ATM.count_bill_or_coin_for(money, withdraw_money)
            money_type = ATM.get_money_type(money, quantity)
            withdraw_line = f"{quantity} {money_type} of {money}.\n"
            withdraw_string = withdraw_string + withdraw_line

            previous_money = money

        return withdraw_string
