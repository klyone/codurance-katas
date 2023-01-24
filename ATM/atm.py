#!/usr/bin/env python3

class Money:
    def __init__(self, quantity, type):
        self.quantity = quantity
        self.type = type

    def get_quantity(self):
        return self.quantity

    def get_type(self):
        return self.type

class ATM:
    def __init__(self, money=[Money(500, "bill"), Money(200, "bill"), Money(100, "bill"), Money(50, "bill"), Money(20, "bill"), Money(10, "bill"), Money(5, "bill"), Money(2, "coin"), Money(1, "coin")]):
        self.allowed_money = money

    @staticmethod
    def __count_bill_or_coin_for(bill_coin, money_list):
        count = 0

        for money in money_list:
            if money.get_quantity() == bill_coin:
                count = count + 1

        return count

    @staticmethod
    def __get_quantity(money):
        return money.get_quantity()

    @staticmethod
    def extract_money_quantity(money_list):
        return list(map(ATM.__get_quantity,money_list))

    def __find_largest_bill_or_coin_for(self, amount):
        for money in self.allowed_money:
            if amount >= money.get_quantity():
                break

        return money

    def withdraw(self, amount):
        withdraw_money = []

        while amount > 0:
            money = self.__find_largest_bill_or_coin_for(amount)
            amount = amount - money.get_quantity()
            withdraw_money.append(money)

        return withdraw_money

    def print_withdraw(self, amount):
        withdraw_money = self.withdraw(amount)
        previous_money = -1
        withdraw_string = ""

        for money in withdraw_money:
            money_quantity = money.get_quantity()
            if previous_money == money_quantity:
                continue

            quantity = ATM.__count_bill_or_coin_for(money_quantity, withdraw_money)
            money_type = money.get_type()
            if quantity > 1:
                money_type = money_type + "s"
            withdraw_line = str(quantity) + " " + money_type + " of " + str(money_quantity)+".\n"
            withdraw_string = withdraw_string + withdraw_line
            previous_money = money_quantity

        return withdraw_string

if __name__ == "__main__":
    atm = ATM()
    print(atm.print_withdraw(434))
