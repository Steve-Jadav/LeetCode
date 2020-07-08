class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 0:
            return 0
        
        maxProfit = 0
        buy = prices[0]
        
        for i in range(1, len(prices)):
            buy = min(prices[i], buy)
            currentProfit = prices[i] - buy
            maxProfit = max(maxProfit, currentProfit)
        
        return maxProfit
