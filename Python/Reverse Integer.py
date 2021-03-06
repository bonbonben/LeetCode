# Given a 32-bit signed integer, reverse digits of an integer.
# Assume that your function returns 0 when the reversed integer overflows.

# Input: 123
# Output: 321

# Input: -123
# Output: -321

# Input: 120
# Output: 21

class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        x_list = list(str(x))
        x_list.reverse()
        if x_list[-1] == '-':
            x_list.pop()
            x_list.insert(0,'-')
        
        r = int(''.join(x_list))
        if (-2**31 > r or r > 2**31-1):
            return 0 
        else:
            return r
