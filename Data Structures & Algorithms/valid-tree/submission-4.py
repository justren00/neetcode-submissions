class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjSet = defaultdict(list)

        for u, v in edges:
            adjSet[u].append(v) 
            adjSet[v].append(u) 

        visited = set() 

        def dfs(u, parent):
            if u in visited:
                return False 
                
            visited.add(u)

            for v in adjSet[u]:
                if v == parent:
                    continue 

                if not dfs(v, u):
                    return False 

            return True 

        return dfs(0, -1) and len(visited) == n
