#!/usr/bin/env python3

def withdraw(amount):
    usd = [200,100]
    current_amount = amount
    ret = []

    while current_amount > 0:
        for i in usd:
            if current_amount >= i:
                current_amount = current_amount - i
                ret.append(i)
                break

    return ret
