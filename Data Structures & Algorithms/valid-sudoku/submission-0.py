class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # creating hashmaps for each criteria we need to check
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                # if empty, skip 
                if board[r][c] == ".":
                    continue

                # check if seen in any of the hashmaps
                if (board[r][c] in cols[c] or 
                    board[r][c] in rows[r] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False
               
                # if not seen before, add to hashmpas
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
       
       # went through the entire board without finding any duplicats
        return True
