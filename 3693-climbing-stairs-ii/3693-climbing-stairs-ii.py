class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:

        dp = [-1]* (n + 1)
        res = self.min_cost(n, costs, dp)
        return res

    def min_cost(self, m , costs, dp):
        if m == 0:
            return 0
        if dp[m] != -1:
            return dp[m] 
        ans = float('inf')

        for j in range(1, 4):
            if m - j >= 0:
                cost = self.min_cost(m-j, costs, dp)+costs[m-1]+j**2
                ans = min(ans, cost)
        dp[m] = ans

        return dp[m]