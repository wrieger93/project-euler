#include <random>
#include <vector>

using std::vector;

/*
 * Returns a*b mod m. Using peasant multiplication to reduce the chance
 * of overflow. See http://en.wikipedia.org/wiki/Ancient_Egyptian_multiplication
 * for the details.
 */
template <class T>
T PeasantMultiply(T a, T b, T m);


/*
 * Returns a^b mod m. Uses fast exponentiation.
 */
template<class T>
T PowerMod(T a, T b, T m);


/*
 * Checks if 'n' is prime using the Miller-Rabin primality test
 * and using the list of numbers in 'tests' to check.
 * See http://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
 * for more details and the pseudocode.
 */
template<class T>
bool MillerRabin(T n, vector<T> tests);


/*
 * Checks if 'num' is prime using the Miller-Rabin primality test.
 * If 'num' is less than a certain constant we only have to check
 * a few possibilities. Otherwise, we check 'k' random choices.
 * See http://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
 * for more details about that mysterious number.
 */
template<class T>
bool IsPrime(T num);


/*
 * Gives a list of all primes up to and including 'n'.
 * Uses the a prime sieve.
 */
vector<int> PrimesUpTo(int n);


/*
 * Returns the next prime after 'n'.
 */
template <class T>
T NextPrime(T n);
