class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        maxLen = 0

        for num in nums:
            if num - 1 not in hashSet:
                l = 1 

                while num + l in hashSet:
                    l += 1

                maxLen = max(l, maxLen)

        return maxLen 