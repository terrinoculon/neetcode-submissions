class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        mProfit = 0
        while (r<len(prices)):
            if prices[r] > prices[l]:
                mProfit = max(mProfit, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return mProfit