class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += (str(len(s)) + '#' + s) 
        print(encoded)
        return encoded


    def decode(self, s: str) -> List[str]:
        i, res = 0, []

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            num = int(s[i:j])
            i = j + 1
            res.append(s[i: i + num])
            i = i + num
        return res






