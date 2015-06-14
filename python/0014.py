# This should be self-explanatory.

# Output: 837799

import functools

MAX = 1000000

def collatz(n):
    return n//2 if n%2 == 0 else 3*n+1

# enable memoization
@functools.lru_cache(maxsize=None)
def collatz_length(n):
    if n == 1:
        return 1
    return 1 + collatz_length(collatz(n))

if __name__=="__main__":
    maxlen = 1
    maxstart = 1
    for i in range(2, MAX+1):
        l = collatz_length(i)
        if l > maxlen:
            maxlen = l
            maxstart = i
    print(maxstart)
