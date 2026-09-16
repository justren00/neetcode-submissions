class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u,v,w in times:
            adj[u].append([v, w]) 

        heap = []
        dist = [math.inf] * (n + 1)

        dist[k] = 0
        heapq.heappush(heap, (0, k))
        time = -1 

        while heap:
            d, u = heapq.heappop(heap) 

            if d > dist[u]:
                continue 

            for v, w in adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(heap, (dist[v], v))
            time += 1

        if math.inf in dist[1:]:
            return -1 

        return max(dist[1:])


