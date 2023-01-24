#!/usr/bin/env python3

import pytest
from atm import *

def test_nothing():
    pass

def test_withdraw_200():
    atm = ATM()
    assert ATM.extract_money_quantity(atm.withdraw(200)) == [200]

def test_withdraw_100():
    atm = ATM()
    assert ATM.extract_money_quantity(atm.withdraw(100)) == [100]

def test_withdraw_300():
    atm = ATM()
    assert ATM.extract_money_quantity(atm.withdraw(300)) == [200, 100]

def test_withdraw_434():
    atm = ATM()
    assert ATM.extract_money_quantity(atm.withdraw(434)) == [200, 200, 20, 10, 2, 2]

def test_print_withdraw_434():
    atm = ATM()
    assert atm.print_withdraw(434) == "2 bills of 200.\n1 bill of 20.\n1 bill of 10.\n2 coins of 2.\n"

def test_check_atm_state():
    atm = ATM()
    assert atm.get_state() == [[500, 2], [200, 3], [100, 4], [50, 12], [20, 20], [10, 50], [5, 100], [2, 250], [1, 500]]
