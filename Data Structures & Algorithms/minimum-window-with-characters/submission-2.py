class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return "" 

        freqT, window = {}, {}
        for ch in t:
            freqT[ch] = freqT.get(ch, 0) + 1 

        have, need = 0, len(freqT) 
        l = 0

        res, resLen = [-1, -1], float('infinity')

        for r in range(len(s)):
            ch = s[r]
            window[ch] = window.get(ch, 0) + 1 

            if ch in freqT and window[ch] == freqT[ch]:
                have += 1 

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1 

                window[s[l]] -= 1 
                if s[l] in freqT and window[s[l]] < freqT[s[l]]: 
                    have -= 1 
                l += 1 

        l, r = res 
        return s[l: r + 1] if resLen != float('infinity') else ""



