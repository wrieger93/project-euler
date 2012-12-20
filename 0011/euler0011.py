"""
i hope this is obvious
"""
def loadarray():
    array = []
    f = open('array.txt','r')
    for line in f:
        array.append([int(x) for x in line.split()])
    f.close()
    return array

def findmax(array):
    ROWS = len(array)
    COLS = len(array[0])
    maxprod = 0
    
    # vertical
    for row in range(ROWS-4):
        for col in range(COLS):
            prod = array[row][col]*array[row+1][col]*\
                   array[row+2][col]*array[row+3][col]
            if prod > maxprod:
                maxprod = prod

    # horizontal
    for row in range(ROWS):
        for col in range(COLS-4):
            prod = array[row][col]*array[row][col+1]*\
                   array[row][col+2]*array[row][col+3]
            if prod > maxprod:
                maxprod = prod

    # diagonal starting from top left
    for row in range(ROWS-4):
        for col in range(COLS-4):
            prod = array[row][col]*array[row+1][col+1]*\
                   array[row+2][col+2]*array[row+3][col+3]
            if prod > maxprod:
                maxprod = prod

    # diagonal starting from top right
    for row in range(ROWS-4):
        for col in range(3,COLS):
            prod = array[row][col]*array[row+1][col-1]*\
                   array[row+2][col-2]*array[row+3][col-3]
            if prod > maxprod:
                maxprod = prod
    
    return maxprod

if __name__=="__main__":
    array = loadarray()
    print(findmax(array)) # answer is 70600674
