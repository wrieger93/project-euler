# This should be self-explanatory.

# Output: 6857

from eulerutils import factor

if __name__ == "__main__":
    factors = factor(600851475143)
    print(max(p for p, e in factors))
