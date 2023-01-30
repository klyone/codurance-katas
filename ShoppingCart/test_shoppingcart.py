#!/usr/bin/env python3

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
