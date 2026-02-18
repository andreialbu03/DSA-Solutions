class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        l, r = 0, 1
        profit = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                dif = prices[r] - prices[l]
                profit = max(profit, dif)
            else:
                l = r
            r += 1

        return profit