"""
i hope this is obvious (for the most part, some parts are kinda condensed)
"""

from functools import reduce

def namescore(name):
    # the 64 is because ord('A') = 65
    # the reduce just takes the product
    return reduce(lambda a,b: a+b, [ord(x)-64 for x in name])

if __name__=="__main__":
    f = open('names.txt','r')
    line = f.readline()
    f.close()

    names = sorted([x[1:-1] for x in line.split(',')])
    print(sum([(i+1)*namescore(names[i]) for i in range(len(names))]))
