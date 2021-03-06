# The DP is explained below.

# Output: 1074

import os
import sys

def loadarray(filename):
    array = []
    with open(filename) as f:
        for line in f:
            array.append([int(x) for x in line.split()])

    return array

"""
Starts from the bottom up. If a max sum goes through an element in the second-
to-last row, the next element is clearly going to be the max of the two below
it. so we can "remove" the last row and make the second-to-last row the new
last row, where the new element is the old element plus the max of the element
beneath it. we can then do the same for the third row from the bottom, etc,
up until the top row.
"""
def findmax(array):
    for row in range(len(array)-2, -1, -1):
        for element in range(len(array[row])):
            array[row][element] += max(array[row+1][element],
                                       array[row+1][element+1])

    return array[0][0]


if __name__=="__main__":
    print(findmax(loadarray(sys.argv[1])))
