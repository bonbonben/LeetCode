# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Input: "cbbd"
# Output: "bb"

# Expand Around Center
# time complexity: O(n^2). Since expanding a palindrome around its center could take O(n) time, the overall complexity is O(n^2)
# space complexity: O(1).
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_left, max_right = 0, 0
        ls = len(s)
        longestSub = ""
        for i in range(ls):
            center = self.expandAroundCenter(s, i, i)
            inBetween = self.expandAroundCenter(s, i, i + 1)
            longestSub = max(longestSub, center, inBetween, key=len)
        return longestSub

    def expandAroundCenter(self, s, left, right):
        ls = len(s)
        while (left >= 0 and right < ls and s[left] == s[right]):
            left -= 1
            right += 1
        return s[left+1:right]
