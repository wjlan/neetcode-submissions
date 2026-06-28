class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        max_profit = 0
        lowest = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > lowest:
                max_profit = max(max_profit, prices[i] - lowest)
            else:
                lowest = min(lowest, prices[i])

        return max_profit
                




        
