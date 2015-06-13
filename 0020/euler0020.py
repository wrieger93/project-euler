# This should be self-explanatory.

# Output: 648

def fact(n):
    tot = 1
    for i in range(2, n+1):
        tot *= i
    return tot

if __name__ == "__main__":
    print(sum(int(x) for x in str(fact(100))))
