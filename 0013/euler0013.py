"""
i hope this is obvious.
it's nice that python has no integer overflow
"""

if __name__=="__main__":
    f = open('nums.txt','r')
    tot = 0
    for line in f:
        tot += int(line)
    print(str(tot)[:10]) # answer is 5537376230
