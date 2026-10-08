class Solution:
    def numDecodings(self, s: str) -> int:
        two = 1
        one = 1 if int(s[len(s) - 1]) > 0 else 0

        for i in range(len(s) - 2, -1, -1):
            temp = one 

            one = 0 

            if int(s[i]) > 0:
                one += temp 
                
                if int(s[i : i + 2]) <= 26:
                    one += two 

            two = temp 

        return one 