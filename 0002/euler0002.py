def fibs_up_to(n):
    fibs = [1, 1]
    while fibs[-1] < n:
        fibs.append(fibs[-1] + fibs[-2])
    return fibs[:-1]

if __name__ == "__main__":
    fibs = fibs_up_to(4000000)
    print sum([x for x in fibs if x % 2 == 0])
