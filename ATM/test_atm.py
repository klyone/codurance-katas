#!/usr/bin/env python3

import pytest
from atm import *

def test_nothing():
    pass

def test_withdraw_200_usd():
    assert withdraw(200) == [200]

def test_withdraw_100_usd():
    assert withdraw(100) == [100]

def test_withdraw_300_usd():
    assert withdraw(300) == [200, 100]

def test_withdraw_434_usd():
    assert withdraw(434) == [200, 200, 20, 10, 2, 2]

def test_print_withdraw_434_usd():
    assert print_withdraw(434) == "2 bills of 200.\n1 bill of 20.\n1 bill of 10.\n2 coins of 2.\n"
