# Given a list of query words, return the number of words that are stretchy.

#Input: S = "heeellooo" words = ["hello", "hi", "helo"]
# Output: 1
# Explanation: We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.

# Run Length Encoding
# For some word, write the head character of every group, and the count of that group.
# For example, for "abbcccddddaaaaa", we'll write the "key" of "abcda", and the "count" [1,2,3,4,5].
# If a word is stretchy. It needs to have the same key as S.
# Let's say we have individual counts c1 = S.count[i] and c2 = word.count[i].
# If c1 < c2, then we can't make the ith group of word equal to the ith word of S by adding characters.
# If c1 >= 3, then we can add letters to the ith group of word to match the ith group of S, as the latter is extended.
# Else, if c1 < 3, then we must have c2 == c1 for the ith groups of word and S to match.

class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        def RLE(S):
            return zip(*[(k, len(list(grp)))
                         for k, grp in itertools.groupby(S)])
        
        R, count = RLE(S)
        ans = 0
        for word in words:
            R2, count2 = RLE(word)
            if R2 != R: continue
            ans += all(c1 >= max(c2, 3) or c1 == c2
                       for c1, c2 in zip(count, count2))
            
        return ans
