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
