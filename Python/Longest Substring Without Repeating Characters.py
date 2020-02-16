# Given a string, find the length of the longest substring without repeating characters.

# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.

# Sliding Window
# time complexity: O(n). Index j will iterate n times.
# space complexity (HashMap): O(min(m, n)).
# space complexity (Table): O(m). m is the size of the charset.
# Commonly used tables are:
# int[26] for Letters 'a' - 'z' or 'A' - 'Z'
# int[128] for ASCII
# int[256] for Extended ASCII
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap = {}
        for i in range(256):
            charMap[i] = -1
        ls = len(s)
        i = max_len = 0
        for j in range(ls):
            # ord() function in Python return an integer representing the Unicode code
            # When charMap[ord(s[j])] >= i, there are duplicate characters in current i, j.
            # If s[j] have a duplicate in the range [i, j) with index j', we can skip all the elements in the range [i, j'] and let i to be j' + 1.
            if charMap[ord(s[j])] >= i:
                i = charMap[ord(s[j])] + 1
            charMap[ord(s[j])] = j
            max_len = max(max_len, j - i + 1)
            #print(i,j,max_len)
        return max_len
