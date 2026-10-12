class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False 

        adj = defaultdict(list)

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        explored = set()

        def dfs(node, parent):
            if node in explored:
                return False 

            explored.add(node)
            for n in adj[node]:
                if n != parent:
                    if not dfs(n, node):
                        return False 

            return True 

        return dfs(0, 0) and len(explored) == n

        