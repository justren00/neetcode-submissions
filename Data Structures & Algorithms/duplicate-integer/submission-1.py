class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool: 
        counts = {}

        for i in nums: 
            if counts.get(i) != None:
                counts[i] = counts[i] + 1
            else:
                counts[i] = 1

        for value in counts.values():
            if value > 1:
                return True
        
        return False
        