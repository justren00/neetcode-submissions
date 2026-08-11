class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)] 
        pairs.sort(reverse=True)

        stack = []

        for pair in pairs:
            speed = (target - pair[0]) / pair[1] 

            if not stack or speed > stack[-1]:
                stack.append(speed)

        return len(stack)

