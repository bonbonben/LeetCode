class Solution:
    def isPalindrome(self, s: str) -> bool:
        # isalnum() checks whether all the characters is a letter or a number
        alnum_s = [t.lower() for t in s if t.isalnum()]
        n = len(alnum_s)
        if n <= 1:
            return True
        mid = int(n / 2)
        for i in range(mid):
            if alnum_s[i] != alnum_s[n - 1 - i]:
                return False
        return True
