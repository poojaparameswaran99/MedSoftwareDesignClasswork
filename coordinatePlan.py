#!/usr/bin/env python3# -*- coding: utf-8 -*-"""Created on Fri Feb  3 13:44:14 2023@author: poojap"""def inputCoordinates():    (coordinate1) = input("Input coordinates for first point on plane in  format (x1, y1): ")    coordinate1 = tuple(int(a) for a in coordinate1.split(","))    (coordinate2) = input("Input coordinates for second point on plane (x2, y2): ")    coordinate2 = tuple(int(a) for a in coordinate2.split(","))    print("\nYou have entered coordinate 1 as: {}".format(coordinate1), " and coordinate 2 as {} \n".format( coordinate2))    return coordinate1, coordinate2def recieveNewX(coordinate1, coordinate2):    x1 = int(coordinate1[0])    x2 = int(coordinate2[0])    x3 = int(input("Input another x coordinate to calculate a y coordinate: "))    return x3def checkNewX(coordinate1, coordinate2, x3):    x1 = int(coordinate1[0])    x2 = int(coordinate2[0])    condition = False    if x1< x3< x2 or x2 < x3 < x1:        condition = True    while condition == False:        print("\nThis is not a valid coordinate! Please input a value between {}".format(x1), "and {} ".format(x2))        x3 = int(input("\nWhat would you like x3 to be? "))        if x1< x3< x2 or x2 < x3 < x1:            condition = True    if condition == True:        return x3    if condition == False:        return False    def findLine(coordinate1, coordinate2):    x1 = coordinate1[0]    x2 = coordinate2[0]    y1 = coordinate1[1]    y2 = coordinate2[1]        # y = mx + b    #Find slope    slo = (y1-y2)/(x1 - x2)    yInt = (x1*y2 - x2*y1)/(x1-x2)    slope = round(slo, 2)    yIntercept = round(yInt,2)    print(slope, yIntercept)    return slope, yIntercept    def findYcoordinate(slope, yIntercept, x3):    y3 = (slope*x3) + yIntercept    print("The y coordinate {} corresponds with {}".format(y3, x3))    return y3    if __name__ == "__main__":    coordinate1, coordinate2 = inputCoordinates()    x3 = recieveNewX(coordinate1, coordinate2)    slope, yIntercept = findLine(coordinate1, coordinate2)    y3 = findYcoordinate(slope, yIntercept, x3)