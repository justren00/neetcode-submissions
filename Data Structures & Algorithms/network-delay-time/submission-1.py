class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u,v,w in times:
            adj[u].append([v, w]) 

        heap = []
        visit = set()
        heapq.heappush(heap, (0, k))
        time = 0

        while heap:
            d, u = heapq.heappop(heap) 

            if u in visit:
                continue 

            visit.add(u)
            time = d

            for v, w in adj[u]:
                if v not in visit:
                    heapq.heappush(heap, (d + w, v))

        return time if len(visit) == n else -1
        