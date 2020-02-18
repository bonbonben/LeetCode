# Given an input string, reverse the string word by word.

# Input: "the sky is blue"
# Output: "blue is sky the"

# Input: "  hello world!  "
# Output: "world! hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.

# Input: "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

class Solution:
    def reverseWords(self, s: str) -> str:
        # remove tail space
        s = s.strip(' ')
        array_s = []
        last = ' '
        #print(s)
        # remove multiple spaces
        for i in range(len(s)):
            if s[i] != ' ':
                array_s.append(s[i])
            else:
                if last != ' ':
                    array_s.append(s[i])
            last = s[i]
        #print(array_s)
        # reverse charactors
        array_s = array_s[::-1]
        #print(array_s)
        ls, pos = len(array_s), 0
        for i in range(ls + 1):
            if i == ls or array_s[i] == ' ':
                self.reverse(array_s, pos, i)
                pos = i + 1
        return ''.join(array_s)
    
    # reverse words
    def reverse(self, array_s, begin, end):
        for i in range(int((end - begin) / 2)):
            array_s[begin + i], array_s[end - i - 1] = array_s[end - i - 1], array_s[begin + i]
