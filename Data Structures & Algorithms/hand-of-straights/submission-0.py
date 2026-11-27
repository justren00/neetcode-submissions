class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False 

        counts = Counter(hand)
        minH = list(counts.keys())
        heapq.heapify(minH)

        while minH:
            first = minH[0]

            for i in range(first, first + groupSize):
                if i not in counts:
                    return False 

                counts[i] -= 1 
                if counts[i] == 0:
                    if i != minH[0]:
                        return False 
                    heapq.heappop(minH) 
                
        return True



        """
        input: a list of integers, a variable groupSize
        output: True if the integers can be arranged into 
        groups of groupSize such that each group is 
        consecutively increasing by 1 
        """ 