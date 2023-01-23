#!/usr/bin/env python3

def find_largest_bill_for_amount(amount):
    allowed_bills = [500, 200, 100, 50, 20, 10, 5, 2, 1]

    for bill in allowed_bills:
        if amount >= bill:
            break

    return bill


def withdraw(amount):
    current_amount = amount
    withdraw_bills = []

    while current_amount > 0:
        bill = find_largest_bill_for_amount(current_amount)
        current_amount = current_amount - bill
        withdraw_bills.append(bill)

    return withdraw_bills
