class Solution:
    def isValid(self, s: str) -> bool:
        paren = {
            ")" : "(",
            "}" : "{",
            "]" : "[",
        }

        stack = []

        for ch in s:
            if ch not in paren.keys():
                stack.append(ch)
            elif ch == ")":
                if not stack:
                    return False 

                top = stack.pop()
                if top != paren[")"]:
                    return False 
            elif ch == "}":
                if not stack:
                    return False 

                top = stack.pop()
                if top != paren["}"]:
                    return False  
            else:
                if not stack:
                    return False 

                top = stack.pop()
                if top != paren["]"]:
                    return False 
        if stack:
            return False
        return True
                