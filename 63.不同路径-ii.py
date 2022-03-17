#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        # State:
        dp = [[0] * m for i in range(n)]
        # Initialization
        for i in range(n): # 行
            if obstacleGrid[i][0]:
                break
            dp[i][0] = 1
        for j in range(m):
            if obstacleGrid[0][j]:
                break
            dp[0][j] = 1
        # Function
        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j]: continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[n - 1][m - 1]
# @lc code=end

