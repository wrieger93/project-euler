# This should be self-explanatory.

# Output:

from eulerutils import is_prime, prime_gen

def rotations(s):
    res = []
    for i in range(len(s)):
        res.append(s[i:] + s[:i])
    return res

if __name__ == "__main__":
    count = 0
    for p in prime_gen():
        if p > 1000000:
            break
        circular = True
        rots = [int(i) for i in rotations(str(p))]
        for rot in rots:
            if not is_prime(rot):
                circular = False
                break
        if circular:
            count += 1
    print(count)
