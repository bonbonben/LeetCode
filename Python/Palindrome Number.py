# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

#class Solution:
#    def isPalindrome(self, x: int) -> bool:
#        if x < 0:
#            return False
#        # <object_name>[<start_index>, <stop_index>, <step>]
#        if x == int(str(x)[::-1]):
#            return True
#        return False

# solve it without converting the integer to a string
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        div = 1
        while x / div >= 10:
            div *= 10
        while x != 0:
            left = int(x / div)
            right = x % 10
            if left != right:
                return False
            x = int((x % div) / 10)
            div /= 100
        return True
