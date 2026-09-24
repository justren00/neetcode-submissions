class Solution:
    def isValid(self, s: str) -> bool:
        paren = {
            ")" : "(",
            "}" : "{",
            "]" : "[",
        }

        stack = []

        for ch in s:
            if ch in paren:
                if stack and stack[-1] == paren[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)

        return True if not stack else False