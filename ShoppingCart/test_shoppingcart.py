#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
from shoppingcart import *
from unittest.mock import call

def testCreateShoppingCart():
    cart = ShoppingCart()

def testPrintEmptyShoppingCart(mocker):
    cart = ShoppingCart()
    mocker_print = mocker.patch("builtins.print")
    cart.printShoppingCart()
    mocker_print.assert_has_calls(
        [
            call("--------------------------------------------"),
            call("| Product name | Price with VAT | Quantity |"),
            call("| -----------  | -------------- | -------- |"),
            call("|------------------------------------------|"),
            call("| Promotion:                               |"),
            call("--------------------------------------------"),
            call("| Total productos: 0                       |"),
            call("| Total price: 0.00 €                      |"),
            call("--------------------------------------------"),
        ]
    )

def testAddItemToShoppingCartAndPrint(mocker):
    cart = ShoppingCart()
    product = Product("Iceberg", 1.55, 15, 21)
    mocker_print = mocker.patch("builtins.print")
    cart.addItem(product)
    cart.printShoppingCart()
    mocker_print.assert_has_calls(
        [
            call("--------------------------------------------"),
            call("| Product name | Price with VAT | Quantity |"),
            call("| -----------  | -------------- | -------- |"),
            call("| Iceberg      | 2.17 €         | 1        |"),
            call("|------------------------------------------|"),
            call("| Promotion:                               |"),
            call("--------------------------------------------"),
            call("| Total productos: 1                       |"),
            call("| Total price: 2.17 €                      |"),
            call("--------------------------------------------"),
        ]
    )

def testAddSingleItemsToShoppingCartAndPrint(mocker):
    cart = ShoppingCart()
    product = Product("Iceberg", 1.55, 15, 21)
    cart.addItem(product)
    product = Product("Tomatoe", 0.52, 15, 21)
    cart.addItem(product)
    product = Product("Chicken", 1.34, 12, 21)
    cart.addItem(product)
    product = Product("Bread  ", 0.71, 12, 10)
    cart.addItem(product)
    product = Product("Corn   ", 1.21, 12, 10)
    cart.addItem(product)
    mocker_print = mocker.patch("builtins.print")
    cart.printShoppingCart()
    mocker_print.assert_has_calls(
        [
            call("--------------------------------------------"),
            call("| Product name | Price with VAT | Quantity |"),
            call("| -----------  | -------------- | -------- |"),
            call("| Iceberg      | 2.17 €         | 1        |"),
            call("| Tomatoe      | 0.73 €         | 1        |"),
            call("| Chicken      | 1.83 €         | 1        |"),
            call("| Bread        | 0.88 €         | 1        |"),
            call("| Corn         | 1.50 €         | 1        |"),
            call("|------------------------------------------|"),
            call("| Promotion:                               |"),
            call("--------------------------------------------"),
            call("| Total productos: 5                       |"),
            call("| Total price: 7.11 €                      |"),
            call("--------------------------------------------"),
        ]
    )

def testAddMultipleItemsToShoppingCartAndPrint(mocker):
    cart = ShoppingCart()
    product = Product("Iceberg", 1.55, 15, 21)
    cart.addItem(product)
    cart.addItem(product)
    cart.addItem(product)
    product = Product("Tomatoe", 0.52, 15, 21)
    cart.addItem(product)
    product = Product("Chicken", 1.34, 12, 21)
    cart.addItem(product)
    product = Product("Bread  ", 0.71, 12, 10)
    cart.addItem(product)
    cart.addItem(product)
    product = Product("Corn   ", 1.21, 12, 10)
    cart.addItem(product)
    mocker_print = mocker.patch("builtins.print")
    cart.printShoppingCart()
    mocker_print.assert_has_calls(
        [
            call("--------------------------------------------"),
            call("| Product name | Price with VAT | Quantity |"),
            call("| -----------  | -------------- | -------- |"),
            call("| Iceberg      | 2.17 €         | 3        |"),
            call("| Tomatoe      | 0.73 €         | 1        |"),
            call("| Chicken      | 1.83 €         | 1        |"),
            call("| Bread        | 0.88 €         | 2        |"),
            call("| Corn         | 1.50 €         | 1        |"),
            call("|------------------------------------------|"),
            call("| Promotion:                               |"),
            call("--------------------------------------------"),
            call("| Total productos: 8                       |"),
            call("| Total price: 12.33 €                     |"),
            call("--------------------------------------------"),
        ]
    )


def testAddTwoItemsToShoppingCartAndPrint(mocker):
    cart = ShoppingCart()
    product = Product("Iceberg", 1.55, 15, 21)
    mocker_print = mocker.patch("builtins.print")
    cart.addItem(product)
    cart.addItem(product)
    cart.printShoppingCart()
    mocker_print.assert_has_calls(
        [
            call("--------------------------------------------"),
            call("| Product name | Price with VAT | Quantity |"),
            call("| -----------  | -------------- | -------- |"),
            call("| Iceberg      | 2.17 €         | 2        |"),
            call("|------------------------------------------|"),
            call("| Promotion:                               |"),
            call("--------------------------------------------"),
            call("| Total productos: 2                       |"),
            call("| Total price: 4.34 €                      |"),
            call("--------------------------------------------"),
        ]
    )

def testDeleteItemAndPrintShoppingCart(mocker):
    cart = ShoppingCart()
    product = Product("Iceberg", 1.55, 15, 21)
    cart.addItem(product)
    cart.deleteItem("Iceberg")
    mocker_print = mocker.patch("builtins.print")
    cart.printShoppingCart()
    mocker_print.assert_has_calls(
        [
            call("--------------------------------------------"),
            call("| Product name | Price with VAT | Quantity |"),
            call("| -----------  | -------------- | -------- |"),
            call("|------------------------------------------|"),
            call("| Promotion:                               |"),
            call("--------------------------------------------"),
            call("| Total productos: 0                       |"),
            call("| Total price: 0.00 €                      |"),
            call("--------------------------------------------"),
        ]
    )

def testAddMultipleItemsWithDiscountToShoppingCartAndPrint(mocker):
    cart = ShoppingCart()
    discount = Discount(5, "PROMO_5")
    product = Product("Iceberg", 1.55, 15, 21)
    cart.addItem(product)
    cart.addItem(product)
    cart.addItem(product)
    product = Product("Tomatoe", 0.52, 15, 21)
    cart.addItem(product)
    product = Product("Chicken", 1.34, 12, 21)
    cart.addItem(product)
    product = Product("Bread  ", 0.71, 12, 10)
    cart.addItem(product)
    cart.addItem(product)
    product = Product("Corn   ", 1.21, 12, 10)
    cart.addItem(product)
    cart.applyDiscount(discount)
    mocker_print = mocker.patch("builtins.print")
    cart.printShoppingCart()
    mocker_print.assert_has_calls(
        [
            call("--------------------------------------------"),
            call("| Product name | Price with VAT | Quantity |"),
            call("| -----------  | -------------- | -------- |"),
            call("| Iceberg      | 2.17 €         | 3        |"),
            call("| Tomatoe      | 0.73 €         | 1        |"),
            call("| Chicken      | 1.83 €         | 1        |"),
            call("| Bread        | 0.88 €         | 2        |"),
            call("| Corn         | 1.50 €         | 1        |"),
            call("|------------------------------------------|"),
            call("| Promotion: 5% off with code PROMO_5      |"),
            call("--------------------------------------------"),
            call("| Total productos: 8                       |"),
            call("| Total price: 11.72 €                     |"),
            call("--------------------------------------------"),
        ]
    )
