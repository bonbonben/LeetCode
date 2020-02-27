# Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

class Solution:
    def toLowerCase(self, str: str) -> str:
        res = []
        gap = ord('a') - ord('A')
        for c in str:
            if ord(c) >= ord('A') and ord(c) <= ord('Z'):
                res.append(chr(ord(c) + gap))
            else:
                res.append(c)
        return ''.join(res)
