#!/usr/bin/env python3

import pytest
from atm import *

def test_nothing():
    pass

def test_withdraw_200_usd():
    assert withdraw(200) == [200]

def test_withdraw_100_usd():
    assert withdraw(100) == [100]
