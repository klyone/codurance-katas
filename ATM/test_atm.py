#!/usr/bin/env python3

import pytest
from atm import *

def test_nothing():
    pass

def test_withdraw_200_usd():
    assert witdhdraw(200) == [200]
