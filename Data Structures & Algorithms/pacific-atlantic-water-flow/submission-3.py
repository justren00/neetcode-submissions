class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r, c, h, ocean):
            if (r < 0 or c < 0 
                or r >= ROWS or c >= COLS
                or (r,c) in ocean
                or heights[r][c] < h):
                return 
                
            ocean.add((r,c))

            d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in d:
                dfs(r + dr, c + dc, heights[r][c], ocean)

        for r in range(ROWS):
            dfs(r, 0, heights[r][0], pacific)
            dfs(r, COLS - 1, heights[r][COLS - 1], atlantic)

        for c in range(COLS):
            dfs(0, c, heights[0][c], pacific)
            dfs(ROWS - 1, c, heights[ROWS - 1][c], atlantic)

        res = []
        for r, c in atlantic:
            if (r, c) in pacific:
                res.append([r,c])

        return res



            

