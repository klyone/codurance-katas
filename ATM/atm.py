#!/usr/bin/env python3

def is_bill(bill_coin):
    if bill_coin > 2:
        return True
    else:
        return False

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


def withdraw(amount):
    current_amount = amount
    withdraw_money = []

    while current_amount > 0:
        money = find_largest_bill_or_coin_for(current_amount)
        current_amount = current_amount - money
        withdraw_money.append(money)

    return withdraw_money

def print_withdraw(amount):
    withdraw_money = withdraw(amount)
    old_w = -1
    withdraw_string = ""

    for w in withdraw_money:
        if old_w == w:
            continue

        num = count_bill_or_coin_for(w, withdraw_money)
        if is_bill(w):
            money_type = "bill"
        else:
            money_type = "coin"

        if num > 1:
            money_type = money_type + "s"

        old_w = w
        tmp = f"{num} {money_type} of {w}.\n"
        withdraw_string = withdraw_string + tmp

    return withdraw_string
