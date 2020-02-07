# Given two strings s and t , write a function to determine if t is an anagram of s.
# Input: s = "anagram", t = "nagaram"
# Output: true

# Sort
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return false
        return sorted(s) == sorted(t)
