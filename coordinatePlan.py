#!/usr/bin/env python3# -*- coding: utf-8 -*-"""Created on Fri Feb  3 13:44:14 2023@author: poojap"""def inputCoordinates():    (coordinate1) = input("Input coordinates for first point on plane in  format (x1, y1): ")    coordinate1 = tuple(int(a) for a in coordinate1.split(","))    (coordinate2) = input("Input coordinates for second point on plane (x2, y2): ")    coordinate2 = tuple(int(a) for a in coordinate2.split(","))    print("You have entered coordinate 1 as: {}".format(coordinate1), " and coordinate 2 as {} \n".format( coordinate2))    return coordinate1, coordinate2def recieveNewX(coordinate1, coordinate2):    x1 = coordinate1[0]    x2 = coordinate2[0]    x3 = input("Input another x coordinate to calculate a y coordinate: ")    x3 = int(x3)    if x1 < x3 < x2:        x3 = x3    else:        print("\nThis is not a valid coordinate! Please input a value between {}".format(x1), "and {} ".format(x2))            x3 = input("\nWhat would you like x3 to be? ")    if __name__ == "__main__":    coordinate1, coordinate2 = inputCoordinates()    recieveNewX(coordinate1, coordinate2)