class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        curMin = float('inf')
        for price in prices:
            if price <curMin:
                curMin = price
            profit = max(profit, price - curMin)
        return profit