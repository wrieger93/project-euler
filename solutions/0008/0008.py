# This should be self-explanatory.

# Output: 23514624000

import functools
import os
import sys

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        num = f.readline()
    max_prod = 0
    for i in range(len(num)-13):
        prod = functools.reduce(lambda x,y: int(x)*int(y), num[i:i+13])
        max_prod = max(prod, max_prod)
    print(max_prod)
