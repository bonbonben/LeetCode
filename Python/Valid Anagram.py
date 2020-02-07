# Given two strings s and t , write a function to determine if t is an anagram of s.
# Input: s = "anagram", t = "nagaram"
# Output: true

# Sort
#class Solution:
#    def isAnagram(self, s: str, t: str) -> bool:
#        if(len(s) != len(t)):
#            return false
#        return sorted(s) == sorted(t)

#Dict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        s_dict = {}
        t_dict = {}
        for ch in s:
            s_dict[ch] = 1 if ch not in s_dict else s_dict[ch] + 1
        for ch in t:
            t_dict[ch] = 1 if ch not in t_dict else t_dict[ch] + 1
        return s_dict == t_dict
