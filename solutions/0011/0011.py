# This should be mostly self-explanatory. Comments where necessary.

# Output: 70600674

import os
import sys

# load the array from a file
def loadarray(filename):
    array = []
    with open(filename) as f:
        for line in f:
            array.append([int(x) for x in line.split()])
    return array

# the meat of the program
def findmax(array):
    rows = len(array)
    cols = len(array[0])
    maxprod = 0

    # vertical
    for row in range(rows-4):
        for col in range(cols):
            prod = array[row][col]*array[row+1][col]*\
                   array[row+2][col]*array[row+3][col]
            if prod > maxprod:
                maxprod = prod

    # horizontal
    for row in range(rows):
        for col in range(cols-4):
            prod = array[row][col]*array[row][col+1]*\
                   array[row][col+2]*array[row][col+3]
            if prod > maxprod:
                maxprod = prod

    # diagonal starting from top left
    for row in range(rows-4):
        for col in range(cols-4):
            prod = array[row][col]*array[row+1][col+1]*\
                   array[row+2][col+2]*array[row+3][col+3]
            if prod > maxprod:
                maxprod = prod

    # diagonal starting from top right
    for row in range(rows-4):
        for col in range(3,cols):
            prod = array[row][col]*array[row+1][col-1]*\
                   array[row+2][col-2]*array[row+3][col-3]
            if prod > maxprod:
                maxprod = prod

    return maxprod

if __name__=="__main__":
    array = loadarray(sys.argv[1])
    print(findmax(array))
