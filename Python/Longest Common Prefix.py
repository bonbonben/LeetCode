# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Input: ["flower","flow","flight"]
# Output: "fl"

# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# horizontal scanning
# time complexity: O(S), S is the sum of all characters in all strings
# space complexity : O(1), we only used constant extra space.

# vertical scanning
# In the worst case there will be n equal strings with length m and the algorithm performs S = m * n character comparisons.
# The worst case is still the same as horizontal scanning.
# In the best case there are at most n * minLen comparisons where minLen is the length of the shortest string in the array.
# time complexity : O(S), S is the sum of all characters in all strings
# space complexity : O(1), we only used constant extra space.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        strs.sort(key = len)
        temp = min(strs, key = len)
        prefix = ''
        for i in range(len(temp)):
            for j in range(1, len(strs[1:])+1):
                if strs[j][i] != temp[i]:
                    return prefix
            prefix += temp[i]
        return prefix
