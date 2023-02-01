#!/usr/bin/env python3

import pytest
from leap_year import *

def test_nothing():
    pass

def test_leap_year_is_divisible_by_4():
    assert is_leap_year(1996)

def test_no_leap_year1():
    assert not is_leap_year(1997)

def test_leap_year_is_divisible_by_400():
    assert is_leap_year(1600)

def test_no_leap_year2():
    assert not is_leap_year(1800)
