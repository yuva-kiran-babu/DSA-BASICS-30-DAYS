class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        best_buy_price = prices[0]
        for i in range(1,len(prices)):
            if prices[i] - best_buy_price > profit:
                profit = prices[i] - best_buy_price
            if  prices[i] < best_buy_price:
                best_buy_price = prices[i]

        return profit
    
