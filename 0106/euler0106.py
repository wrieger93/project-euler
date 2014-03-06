from itertools import combinations

def subset_pairs(n, k):
    toret = []
    lst = set(range(1,n+1))
    for a in combinations(lst, k):
        lst2 = lst - set(a)
        for b in combinations(lst2, k):
            if a < b:
                toret.append((a,b))
            else:
                toret.append((b,a))
    return set(toret)

def count_valid(pairs):
    tot = 0
    for pair in pairs:
        count = 0
        for i in range(len(pair[0])):
            if pair[0][i] < pair[1][i]:
                count += 1
        if 0 < count < len(pair[0]):
            tot += 1
    return tot

if __name__ == "__main__":
    tot = 0
    for i in range(2, 7):
        tot += count_valid(subset_pairs(12, i))
    print tot
