"""
i should probably be doing this in c++ but whatevs
"""

lengths = {1: 1}
MAX = 1000000

def collatz(n):
    return n//2 if n%2 == 0 else 3*n+1

def makechain(n):
    chain = [n]
    while chain[-1] != 1 and chain[-1] not in lengths.keys():
        chain.append(collatz(chain[-1]))
        
    for i in range(1,len(chain)):
        lengths[chain[-(i+1)]] = lengths[chain[-1]] + i

if __name__=="__main__":
    maxlen = 0
    for i in range(2,MAX):
        makechain(i)

    maxlength = 0
    maxnum = 0
    for k,v in lengths.items():
        if v > maxlength and k < MAX:
            maxlength = v
            maxnum = k

    print(maxnum) # answer is 837799
