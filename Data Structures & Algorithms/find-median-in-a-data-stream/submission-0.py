class MedianFinder:

    def __init__(self):
        self.minRight = []
        self.maxLeft = []

    def addNum(self, num: int) -> None:
        if self.minRight: 
            topRight = self.minRight[0]
        else:
            topRight = 0 

        if num > topRight: 
            heapq.heappush(self.minRight, num)
        else:
            heapq.heappush(self.maxLeft, -num)

        if abs(len(self.minRight) - len(self.maxLeft)) > 1:
            if len(self.minRight) > len(self.maxLeft):
                top = heapq.heappop(self.minRight)   
                heapq.heappush(self.maxLeft, -top) 
            else:
                top = heapq.heappop(self.maxLeft)   
                heapq.heappush(self.minRight, -top)
        

    def findMedian(self) -> float:
        if len(self.minRight) == len(self.maxLeft):
            left = -self.maxLeft[0]
            right = self.minRight[0]
            return (left + right) / 2 

        if len(self.minRight) > len(self.maxLeft):
            return self.minRight[0]
        else:
            return -self.maxLeft[0]
        