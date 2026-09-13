class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [ i for i in range(n)]
        rank = [1] * n

        def find(u):
            res = u
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res 

        def union(u,v):
            pu,pv = find(u), find(v)

            if pu == pv:
                return 0

            if rank[pu] > rank[pv]:
                par[pv] = pu
                rank[pu] += rank[pv] 
            else:
                par[pu] = pv
                rank[pv] += rank[pu] 
            return 1
        res = n
        for u, v in edges:
            res -= union(u,v)
        return res