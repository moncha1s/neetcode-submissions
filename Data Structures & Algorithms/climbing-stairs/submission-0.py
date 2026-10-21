class Solution:
    def climbStairs(self, n: int) -> int:
        # we're given in the problem statement that 1 <= n <= 45
        if n == 1:
            return 1
        end = n + 1
        dp = [-1] * (end)

        #base cases
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2


        for i in range(3, end):
            dp[i] = dp[i-1] + dp[i-2]


        numStairs = dp[n]
        return numStairs if (numStairs != -1) else -2