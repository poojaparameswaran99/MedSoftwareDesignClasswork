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
    
    
@pytest.mark.parametrize("coor1, coor2, expected",
                         [((-1,5), (3,7), (1/2,2), (11/2))),
                          ((1,5), (4,10), (5/3, 2), (10/3,2))),
                          ((10,10), (5,5), (1, 0))])
def test_findLine(coor1, coor2, expected):
    from coordinatePlan import findLine
    
    #Act
    answer = findLine(coor1, coor2)
    
    #assert 
    assert answer == pytest.approx(expected)
    
    
@pytest.mark.parametrize("slope, yInt, x3, expected",
                         [((1/2,2), (11/2, 3), 7),
                          ((5/3, 2), (10/3, 3) , 8.34)]
                         )
def test_findYcoordinate(slope, yInt, x3, expected):
    from coordinatePlan import findYcoordinate

    #Act
    answer = findYcoordinate(slope, yInt, x3)
    
    # Assert
    assert answer ==pytest.approx(expected)
    
    