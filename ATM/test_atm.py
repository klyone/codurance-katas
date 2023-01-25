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
    atm = ATM(initial_amount = [2, 3, 4, 12, 20, 50, 100, 250, 500])
    assert atm.get_state() == [[500, 2], [200, 3], [100, 4], [50, 12], [20, 20], [10, 50], [5, 100], [2, 250], [1, 500]]

def test_final_withdraw():
    atm = ATM(initial_amount = [2, 3, 5, 12, 20, 50, 100, 250, 500])
    atm.print_withdraw(1725)
    atm.print_withdraw(1825)
    assert atm.get_state() == [[500, 0], [200, 0], [100, 0], [50, 0], [20, 0], [10, 6], [5, 98], [2, 250], [1, 500]]
