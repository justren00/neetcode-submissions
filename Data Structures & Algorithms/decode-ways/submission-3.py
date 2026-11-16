class Solution:
    def numDecodings(self, s: str) -> int:
        one, two = 1, 1

        for i in range(len(s) - 1, -1, -1):
            temp = one 

            one = 0
            if int(s[i]) > 0:
                one += temp 

                if i + 2 <= len(s) and int(s[i : i + 2]) <= 26:
                    one += two 
            
            two = temp 
              
        return one 
                    