class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = {}
        tdict = {}

        for ch in s:
            sdict[ch] = sdict.get(ch, 0) + 1 

        for ch in t:
            tdict[ch] = tdict.get(ch, 0) + 1

        if sdict == tdict:
            return True
        
        return False


