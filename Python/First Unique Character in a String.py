# Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

# s = "leetcode", return 0.
# s = "loveleetcode", return 2.

# time complexity: O(N) since we go through the string of length N two times.
# space complexity: O(N) since we have to keep a hash map with N elements.
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # build hash map : character and how often it appears
        count = collections.Counter(s)
        #print(count)
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1
