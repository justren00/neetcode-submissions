class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(open_c, close_c, cur):
            if open_c + close_c == 2 * n:
                res.append("".join(cur))

            if open_c < n:
                cur.append("(")
                dfs(open_c + 1, close_c, cur) 
                cur.pop()

            if close_c + 1 <= open_c:
                cur.append(")")
                dfs(open_c, close_c + 1, cur) 
                cur.pop()
            
        dfs(0, 0, [])
        return res