"""
i don't think any explanation is needed
"""

from itertools import permutations

def hasprop(n):
    return int(str(n)[1:4])%2 == 0 and\
           int(str(n)[2:5])%3 == 0 and\
           int(str(n)[3:6])%5 == 0 and\
           int(str(n)[4:7])%7 == 0 and\
           int(str(n)[5:8])%11 == 0 and\
           int(str(n)[6:9])%13 == 0 and\
           int(str(n)[7:10])%17 == 0

if __name__=="__main__":
    tot = 0
    for perm in permutations("0123456789"):
        num = int(''.join(perm))
        if num > 10**9 and hasprop(num):
            tot += num

    print(tot) # answer is 16695334890
