class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()
        fresh = 0
        time = 0

        def addRoom(r, c):
            nonlocal fresh
            if (r < 0 or c < 0
                or r == ROWS or c == COLS
                or (r,c) in visit or grid[r][c] != 1):
                return 
            q.append([r,c])
            visit.add((r,c))
            grid[r][c] = 2
            fresh -= 1
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r,c])
                    visit.add((r,c)) 
                if grid[r][c] == 1:
                    fresh += 1

        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1) 
            time += 1 

        return time if fresh == 0 else -1
        
