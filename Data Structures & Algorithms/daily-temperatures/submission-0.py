class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brute force: iterating through the list and for each element
        # iterating thru the list until we encounter a larger number
        # Time: O(n^2) 
        n = len(temperatures)
        stack = []
        res = [0] * n

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                popped = stack.pop()

                res[popped] = i - popped 

            stack.append(i)

        return res
