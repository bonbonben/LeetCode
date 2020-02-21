# The input will be two strings, and the output needs to be the length of the longest uncommon subsequence.
# If the longest uncommon subsequence doesn't exist, return -1.

# Input: "aba", "cdc"
# Output: 3
# Explanation: The longest uncommon subsequence is "aba" (or "cdc"), 
# because "aba" is a subsequence of "aba", 
# but not a subsequence of any other strings in the group of two strings.

class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        return -1 if a == b else max(len(a), len(b))
