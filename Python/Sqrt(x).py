# Input: 4
# Output: 2

# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.

class Solution:
    def mySqrt(self, x: int) -> int:
        # sqrt(x) = 2 * sqrt(x / 4) for n % 4 == 0
        # sqrt(x) = 1 + 2 * sqrt(x / 4) for n % 4 != 0
        if x == 0:
            return 0
        if x < 4:
            return 1
        res = 2 * self.mySqrt(x / 4)
        # (res + 1) * (res + 1) >= 0 for avoiding overflow
        if (res + 1) * (res + 1) <= x and (res + 1) * (res + 1) >= 0:
            return res + 1
        return  res
