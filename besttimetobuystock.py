'''class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a=len(prices)
        b=min(prices)
        profit=[0]*a
        buy=prices.index(b)
        for i in range(buy,a):
            if prices[i]>b:
               profit[i]= prices[i]-b
        return max(profit)'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        profit = 0

        for p in prices[1:]:
            if buy_price > p:
                buy_price = p
            
            profit = max(profit, p - buy_price)
        
        return profit