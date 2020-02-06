# Given an array of strings, group anagrams together.
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output: [["eat","tea","ate"],["tan","nat"],["bat"]]

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()
