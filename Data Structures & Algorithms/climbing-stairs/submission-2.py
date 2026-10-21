class Solution:
    def climbStairs(self, n: int) -> int:
        # we're given in the problem statement that 1 <= n <= 45
        if n <= 2:
            return n

        dp = [-1] * 3

        #base cases
        dp[0] = 1
        dp[1] = 2

        for i in range(3, n + 1):
            dp[2] = dp[1] + dp[0]
            dp[0] = dp[1]
            dp[1] = dp[2]

        numStairs = dp[2]
        return numStairs