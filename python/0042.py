"""
t_n = n(n+1)/2, or n^2 + n - 2t_n = 0, so n = (-1 + sqrt(1 + 8t_n))/2.
we can check if t_n is a triangular number by checking if ^ is an integer.
"""

from math import sqrt

def val(word):
    return sum([ord(x)-64 for x in word]) #-64 because ord('A') = 65

def istriangleword(word):
    tot = val(word)
    if (sqrt(1+8*tot)-1)%2 == 0:
        return 1
    return 0

if __name__=="__main__":
    f = open('words.txt','r')
    line = f.readline()
    f.close()

    words = [x[1:-1] for x in line.split(',')]
    tot = 0
    for word in words:
        if istriangleword(word):
            tot += 1

    print(tot) # answer is 162
