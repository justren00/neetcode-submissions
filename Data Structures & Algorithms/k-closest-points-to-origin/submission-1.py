class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for coordinate in points:
            distance = coordinate[0]**2 + coordinate[1]**2
            
            heapq.heappush(heap, (-distance, coordinate)) 

            if len(heap) > k:
                    heapq.heappop(heap) 

        res = [heapq.heappop(heap)[1] for _ in range(len(heap))]    
        return res