class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a=len(prices)
        b=min(prices)
        profit=[0]*a
        buy=prices.index(b)
        for i in range(buy,a):
            if prices[i]>b:
               profit[i]= prices[i]-b
        return max(profit)