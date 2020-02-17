# Count the number of prime numbers less than a non-negative number, n.

# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [True] * (n + 1)
        for i in range(2, int(n ** 0.5) + 1):
            if isPrime[i]:
                # range(start, stop, step)
                # step: An integer number specifying the incrementation. Default is 1
                for j in range(i * i, n + 1, i):
                    isPrime[j] = False
        #print([x for x in range(2, n + 1) if isPrime[x]])
        count = 0
        for i in range(2, n):
            if isPrime[i]:
                count += 1
        return count
