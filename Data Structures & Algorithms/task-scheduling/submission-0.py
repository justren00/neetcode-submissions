class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}

        for task in tasks:
            counts[task] = counts.get(task, 0) + 1

        heap = [(-value, key) for key, value in counts.items()]

        heapq.heapify(heap)
        queue = deque()
        time = 0
        
        while heap or queue: 
            time += 1 

            if queue and queue[0][2] <= time:
                remaining, task, schedule = queue.popleft()
                heapq.heappush(heap, (remaining, task))

            if heap: 
                remaining, task = heapq.heappop(heap) 
                remaining += 1 

                if remaining != 0:
                    queue.append((remaining, task, time + n + 1)) 


        return time

