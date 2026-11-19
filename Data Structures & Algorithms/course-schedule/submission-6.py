class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for a, b in prerequisites:
            adj[a].append(b) 

        path = set()

        def dfs(c):
            # terminal node
            if not adj[c]:
                return True 
            
            # already seen --> cycle 
            if c in path:
                return False 

            path.add(c)

            for pre in adj[c]:
                if not dfs(pre):
                    return False 

            path.remove(c)
            adj[c] = []
            return True 

        for c in range(numCourses):
            if not dfs(c):
                return False 
        return True
            