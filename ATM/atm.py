#!/usr/bin/env python3

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
