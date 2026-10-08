class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                print(i)
                print(j)
                if j + 1 == n and i + 1 == m:
                    print(i)
                    print(j)
                    dp[i][j] = 1
                    continue 

                right = 0 if j + 1 >= n else dp[i][j + 1]
                down = 0 if i + 1 >= m else dp[i + 1][j]

                dp[i][j] = right + down 

        return dp[0][0]
