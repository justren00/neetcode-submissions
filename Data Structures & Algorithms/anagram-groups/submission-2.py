class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            signature = [0] * 26
            for ch in s:
                signature[ord(ch) - 97] += 1
            code = ', '.join(map(str, signature)) 
            anagrams[code].append(s)

        return list(anagrams.values())