class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        result = prices[:]
        stack = []

        for j in range(len(prices)):
            while stack and prices[j] <= prices[stack[-1]]:
                i = stack.pop()
                result[i] = prices[i] - prices[j]

            stack.append(j)

        return result