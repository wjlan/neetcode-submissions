class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        i = 0
        for j in range(1, len(prices)):
            if prices[j] > prices[i]:
                max_profit = max(max_profit, prices[j] - prices[i])
            else:
                i = j
        
        return max_profit
            
        
        