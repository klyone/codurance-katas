#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

# Get the original implementation at:
# https://realpython.com/python-rounding/#:~:text=To%20implement%20the%20%E2%80%9Crounding%20up,equal%20to%20a%20given%20number.
def round_up(n, decimals=0):
    multiplier = 10 ** (decimals+2)
    n_int = int(n * multiplier)
    return math.ceil(n_int / 100.0) / (multiplier / 100.0)

class Discount:
    def __init__(self, amount, id):
        self.amount = amount
        self.id = id

    def getId(self):
        return self.id

    def getAmount(self):
        return self.amount

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
        self.discount = None

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
                ticket_line = "| " + str(product_name)
                ticket_line = ticket_line.ljust(len(ticket_line)+(13-len(product_name))," ")
                ticket_line = ticket_line + "| " + str("{0:.2f}".format(product_final_price)) + " €"
                ticket_line = ticket_line.ljust(len(ticket_line)+(13-len(str("{0:.2f}".format(product_final_price))))," ")
                ticket_line = ticket_line + "| " + str(number_of_products)
                ticket_line = ticket_line.ljust(len(ticket_line)+(9-len(str(number_of_products)))," ")
                ticket_line = ticket_line +"|"
                print(ticket_line)
                processed_products.append(product_name)
                total_price = total_price + (product_final_price * number_of_products)

            total_products = total_products + 1

        print("|------------------------------------------|")
        promo_line = "| Promotion: "
        if self.discount != None:
            promo_line = promo_line + str(self.discount.getAmount()) + "% off with code "+self.discount.getId()
            total_price = round_up(total_price - (total_price * self.discount.getAmount()/100.0),2)

        promo_line = promo_line.ljust(len(promo_line)+(43-len(promo_line)), " ")
        promo_line = promo_line + "|"
        print(promo_line)
        print("--------------------------------------------")
        total_line = "| Total productos: " + str(total_products)
        total_line = total_line.ljust(len(total_line)+(42-18-len(str(total_products))))
        total_line = total_line + "|"
        print(total_line)
        total_line = "| Total price: " + str("{0:.2f}".format(total_price)) + " €"
        total_line = total_line.ljust(len(total_line)+(42-16-len(str("{0:.2f}".format(total_price)))))
        total_line = total_line + "|"
        print(total_line)
        print("--------------------------------------------")

    def addItem(self, product):
        self.products.append(product)

    def deleteItem(self, product_name):
        for p in self.products:
            if product_name == p.getName():
                self.products.remove(p)
                break

    def applyDiscount(self, discount):
        self.discount = discount
