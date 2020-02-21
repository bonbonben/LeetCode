# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

# Input: "aba"
# Output: True

# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.

#class Solution:
#    def validPalindrome(self, s: str) -> bool:
#        return self.validPalindromeHelper(s, 0, len(s) - 1, 1)
#
#    def validPalindromeHelper(self, s, left, right, budget):
#        # budget can be more than 1
#        while right >= 0 and left <= right and s[left] == s[right]:
#            left += 1
#            right -= 1
#        if right < 0 or left >= right:
#            return True
#        if budget == 0:
#            return False
#        budget -= 1
#        return self.validPalindromeHelper(s, left + 1, right, budget) or self.validPalindromeHelper(s, left, right - 1, budget)

# time complexity: O(n).
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        s = s.lower()
        print("s = ", s)
        while left < right:
            if(s[left] != s[right]):
                return False
            left += 1
            right -= 1
        return True
    
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if(s[left] != s[right]):
                return self.isPalindrome(s[left:right]) or self.isPalindrome(s[left+1:right+1])
            left += 1
            right -= 1
        return True
