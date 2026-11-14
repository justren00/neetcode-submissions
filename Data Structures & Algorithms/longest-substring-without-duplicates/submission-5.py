class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        res = 0 

        l = 0       
        for r in range(len(s)):
            if s[r] in unique: 
                while s[r] in unique:
                    unique.remove(s[l])
                    l += 1

            unique.add(s[r])
            res = max(res, r - l + 1)
        return res