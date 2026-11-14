class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count the frequencies 
        freqs = {}

        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1

        # create the buckets 
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in freqs.items():
            buckets[freq].append(num)

        # form the result
        res = []

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
            if len(res) == k:
                return res