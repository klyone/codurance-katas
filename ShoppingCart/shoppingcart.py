#!/usr/bin/env python3

import math

# Get the original implementation at:
# https://realpython.com/python-rounding/#:~:text=To%20implement%20the%20%E2%80%9Crounding%20up,equal%20to%20a%20given%20number.
def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

class Product:
    def __init__(self, name, price, revenue, vat):
        self.name = name
        self.price = price
        self.revenue = revenue
        self.vat = vat

    def getName(self):
        return self.name

    def getPriceWithRevenue(self):
        return round_up(self.price + (self.price*(self.revenue/100.0)), 2)

    def getFinalPrice(self):
        p = self.getPriceWithRevenue()
        return round_up(p + (p*(self.vat/100.0)), 2)


class ShoppingCart:
    def __init__(self):
        self.products = []

    def __getNumberOfSpecificProduct(self, product_name):
        n = 0

        for p in self.products:
            if p.getName() == product_name:
                n = n + 1

        return n

    def printShoppingCart(self):
        total_products = 0
        total_price = 0.00
        processed_products = []

        print("--------------------------------------------")
        print("| Product name | Price with VAT | Quantity |")
        print("| -----------  | -------------- | -------- |")

        for p in self.products:
            product_name = p.getName()

            if not product_name in processed_products:
                product_final_price = p.getFinalPrice()
                number_of_products = self.__getNumberOfSpecificProduct(product_name)
                ticket_line = "| " + str(product_name) + "      | " + str("{0:.2f}".format(product_final_price)) +" €         | " + str(number_of_products) + "        |"
                print(ticket_line)
                processed_products.append(product_name)
                total_price = total_price + (product_final_price * number_of_products)

            total_products = total_products + 1

        print("|------------------------------------------|")
        print("| Promotion:                               |")
        print("--------------------------------------------")
        print("| Total productos: " + str(total_products) + "                       |")
        print("| Total price: " + str("{0:.2f}".format(total_price)) + " €                      |")
        print("--------------------------------------------")

    def addItem(self, product):
        self.products.append(product)
