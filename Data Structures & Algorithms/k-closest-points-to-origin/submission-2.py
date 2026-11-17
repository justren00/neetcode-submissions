class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        max heap, calculate distance with sqrt(x1^2 + y1^2) for each
        coordinate and add it to the heap and when the size of the heap
        exceeds k, pop the top 
        your left with the k smallest distances 
        """
        def euclidian(coord):
            return math.sqrt((coord[0] ** 2) + (coord[1] ** 2)) 

        heap = [] 
         
        for point in points:
            heapq.heappush(heap, (-1 * euclidian(point), point))

            if len(heap) > k:
                heapq.heappop(heap) 

        res = [heapq.heappop(heap)[1] for _ in range(len(heap))]
        return res
