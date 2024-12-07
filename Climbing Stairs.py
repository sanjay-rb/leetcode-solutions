class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {1:1, 2:2}
        next = 3
        while n not in dp:
            dp[next] = dp[next-1] + dp[next-2]
            next += 1
        return dp[n]