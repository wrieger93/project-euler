#include <algorithm>
#include <climits>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>

#include "primes.hpp"

using std::cout;
using std::string;
using std::vector;

/*
 * Checks if a number 'num' contains 200 as a substring.
 */
template <class T>
bool Contains200(T num) {
    std::ostringstream convert;
    convert << num;
    string numstr = convert.str();
    return numstr.find("200") != string::npos;
}

template <class T>
vector<T> DigitChanges(T n) {
    std::ostringstream convert;
    convert << n;
    string numstr = convert.str();

    vector<T> changes;
    for(size_t index = 0; index < numstr.size(); ++index) {
        T pow10 = T(std::pow(10, index));
        T lowerpart = n % pow10;
        T upperpart = n / pow10;
        T digit = upperpart % 10;
        int newdigit = 0; // (index == numstr.size() - 1) ? 1 : 0;
        for(; newdigit <= 9; ++newdigit) {
            if(newdigit == digit) {
                continue;
            }
            changes.push_back((upperpart-digit+newdigit)*pow10 + lowerpart);
        }
    }
    return changes;
}

template <class T>
bool PrimeProof(T n) {
    for(auto i : DigitChanges(n)) {
        if(IsPrime(i)) {
            return false;
        }
    }
    return true;
}

template <class T>
T NextSqube(T sqube) {
    long long minsqube = LLONG_MAX;

    long long q_max = NextPrime((long long)std::floor(std::pow(sqube, 1.0/3)));
    long long q = 2;
    while(q <= q_max) {
        long long p = NextPrime((long long)std::floor(std::sqrt(sqube/std::pow(q, 3))));
        if(p != q) {
            long long newsqube = p*p*q*q*q;
            if(newsqube < minsqube) {
                minsqube = newsqube;
            }
        }
        q = NextPrime(q);
    }
    return minsqube;
}

template <class T>
vector<T> SqubesUpTo(T n) {
    vector<long long> primes = PrimesUpTo((long long)(std::ceil(std::sqrt(n))));
    vector<T> squbes;
    for(T p : primes) {
        for(T q : primes) {
            if(p != q) {
                T sqube = p*p*q*q*q;
                if(sqube < n) {
                    squbes.push_back(sqube);
                }
                else {
                    break;
                }
            }
        }
    }
    std::sort(squbes.begin(), squbes.end());
    return squbes;
}

int main() {
    int count = 0;
    for(long long sqube : SqubesUpTo(300000000000LL)) {
        if(Contains200(sqube) && PrimeProof(sqube)) {
            ++count;
            if(count == 200) {
                cout << sqube << "\n";
                return 0;
            }
        }
    }
    cout << "didn't find 200 squbes\n";
    return 0;
}
