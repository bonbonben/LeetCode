# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
# If the last word does not exist, return 0.

# Input: "Hello World"
# Output: 5

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0:
            return 0
        temp = s.split(' ')
        temp = [t for t in temp if len(t) > 0]
        if len(temp) == 0:
            return 0
        else:
            return len(temp[-1])
