# Write a program to check whether a given number is an ugly number.
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

# Input: 6
# Output: true
# Explanation: 6 = 2 × 3

# Input: 8
# Output: true
# Explanation: 8 = 2 × 2 × 2

# Input: 14
# Output: false 
# Explanation: 14 is not ugly since it includes another prime factor 7.

class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        divisors = [2, 3, 5]
        for d in divisors:
            while num % d == 0:
                num /= d
        if num == 1:
            return True
        else:
            return False
