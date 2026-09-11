class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, ocean):
            if (r, c) in ocean:
                return 

            ocean.add((r,c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]] 

            for dr, dc in directions:
                row, col = r + dr, c + dc 
                if (row in range(ROWS)
                    and col in range(COLS)
                    and heights[row][col] >= heights[r][c]):
                    dfs(row, col, ocean)
        
        for c in range(COLS): 
            dfs(0, c, pacific)
            dfs(ROWS - 1, c, atlantic)  

        for r in range(ROWS):
            dfs(r, 0, pacific)
            dfs(r, COLS - 1, atlantic)   

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        return res


        