class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            signature = [0] * 26
            for ch in s:
                signature[ord(ch) - 97] += 1 
                
            anagrams[tuple(signature)].append(s)

        return list(anagrams.values())