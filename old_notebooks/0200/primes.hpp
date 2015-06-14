#ifndef PRIMES_HPP
#define PRIMES_HPP

#include <algorithm>
#include <random>
#include <vector>

using std::vector;

/*
 * Returns a*b mod m. Using peasant multiplication to reduce the chance
 * of overflow. See http://en.wikipedia.org/wiki/Ancient_Egyptian_multiplication
 * for the details.
 */
template <class T>
T PeasantMultiply(T a, T b, T m) {
    T min = (a < b ? a : b) % m;
    T max = (a < b ? b : a) % m;
    T tot = 0;
    while(min > 0) {
        if(min % 2 == 1) {
            tot += max;
            tot %= m;
        }
        min /= 2;
        max = (2 * max) % m;
    }
    return tot;
}

/*
 * Returns a^b mod m. Uses fast exponentiation.
 */
template<class T>
T PowerMod(T a, T b, T m) {
    if(b == 0) {
        return T(1);
    }
    if(b == 1) {
        return a % m;
    }
    T pow = PowerMod(a, b/2, m) % m;
    T toret = (b % 2 == 0 ? T(1) : a) % m;
    toret = PeasantMultiply(toret, pow, m);
    toret = PeasantMultiply(toret, pow, m);
    return toret;
}


/*
 * Checks if 'n' is prime using the Miller-Rabin primality test
 * and using the list of numbers in 'tests' to check.
 * See http://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
 * for more details and the pseudocode.
 */
template<class T>
bool MillerRabin(T n, vector<T> tests) {
    T s = 0;
    T d = n-1;
    while(d % 2 == 0) {
        ++s;
        d /= 2;
    }
    for(auto a : tests) {
        T x = PowerMod(a, d, n);
        if(x == 1 or x == n-1) {
            continue;
        }
        bool flag = false;
        for(int i = 0; i < s-1; ++i) {
            x = PowerMod(x, T(2), n);
            if(x == 1) {
                return false;
            }
            if(x == n-1) {
                flag = true;
                break;
            }
        }
        if(!flag) {
            return false;
        }
    }
    return true;
}


template <class T>
vector<T> PrimesUpTo(T);
/*
 * Checks if 'num' is prime using the Miller-Rabin primality test.
 * If 'num' is less than a certain constant we only have to check
 * a few possibilities. Otherwise, we check 40 random choices.
 * See http://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
 * for more details about that mysterious number.
 */
template<class T>
bool IsPrime(T num) {
    if(num < 2) {
        return false;
    }
    static vector<T> small_primes = PrimesUpTo((T)10000);
    if(std::find(small_primes.begin(), small_primes.end(), num) != small_primes.end()) {
        return true;
    }
    static vector<T> tests = {2, 3, 5, 7, 11, 13, 17};
    static std::default_random_engine gen;
    static std::uniform_int_distribution<T> dist(2, num-1);
    if(num < 341550071728321LL) {
        return MillerRabin(num, tests);
    }
    else {
        vector<T> random_tests;
        for(int i = 0; i < 40; ++i) {
            random_tests.push_back(dist(gen));
        }
        return MillerRabin(num, random_tests);
    }
    return false;
}


/*
 * Gives a list of all primes up to and including 'n'.
 * Uses a prime sieve.
 */
template <class T>
vector<T> PrimesUpTo(T n) {
    vector<bool> sieve = {false, false};
    for(T i = 2; i <= n; ++i) {
        sieve.push_back(true);
    }
    T p = 2;
    while(p * p < n) {
        for(T i = p*p; i <= n; i += p) {
            sieve[i] = false;
        }
        ++p;
        while(!sieve[p]) {
            ++p;
        }
    }
    vector<T> primes;
    for(T i = 0; i <= n; ++i) {
        if(sieve[i]) {
            primes.push_back(i);
        }
    }
    return primes;
}


/*
 * Returns the next prime after 'n'.
 */
template <class T>
T NextPrime(T n) {
    if(n == 0 or n == 1) {
        return 2;
    }
    if(n == 2) {
        return 3;
    }
    T p = n + (n % 2 == 0 ? 1 : 2);
    while(!IsPrime(p)) {
        p += 2;
    }
    return p;
}

#endif
