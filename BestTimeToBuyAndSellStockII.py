class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for i in range(1, len(prices)):
            profit = 0
            if prices[i] > prices[i-1]:
                profit = prices[i] - prices[i-1]
            maxProfit += profit
        
        return maxProfit
