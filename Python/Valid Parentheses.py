# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Input: "(]"
# Output: false

# Input: "([)]"
# Output: false

class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for c in s:
            if c in ["(", "[", "{"]:
                stk.append(c)
            else:
                if len(stk) == 0:
                    return False
                p = stk.pop()
                if (p == "(" and c != ")" or p == "[" and c != "]" or p == "{" and c != "}"):
                    return False
        if len(stk) == 0:
            return True 
        else:
            return False
