#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 09:08:00 2023

@author: poojap
"""

import pytest

@pytest.mark.parametrize("coor1, coor2, x3, expected",
                         [((1,5), (4,10), 3, 3),
                          ((10,10), (4,1), 7, 7)])
def test_checkNewX(coor1, coor2,x3, expected):
    from coordinatePlan import checkNewX
    
    #Act
    answer = checkNewX(coor1, coor2 , x3)
    #Assert 
    assert answer == expected
    
    