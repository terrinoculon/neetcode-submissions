class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        curMin = float(1e7)
        for price in prices:
            if price <curMin:
                curMin = price
            profit = max(profit, price - curMin)
        return profit