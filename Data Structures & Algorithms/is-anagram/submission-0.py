class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = {}
        hash_t = {}

        for ch in s:
            if hash_s.get(ch) == None:
                hash_s[ch] = 1
            else:
                hash_s[ch] = hash_s[ch] + 1
        
        for ch in t:
            if hash_t.get(ch) == None:
                hash_t[ch] = 1
            else:
                hash_t[ch] = hash_t[ch] + 1
        
        result = hash_s == hash_t
        return result