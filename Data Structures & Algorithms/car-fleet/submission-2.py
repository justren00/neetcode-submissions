class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(position[i], speed[i]) for i in range(len(position))] 

        pairs.sort(reverse=True)
        stack = []

        for pair in pairs:
            eta = (target - pair[0]) / pair[1]

            if not stack or stack[-1] < eta:
                stack.append(eta)

        return len(stack)

        
        