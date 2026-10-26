class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit=0
        l,r=0,1
        while r<len(prices):
            if prices[l]<prices[r]:
                total=prices[r]-prices[l]
                max_profit=max(max_profit,total)
            else:
                l=r
            r+=1
        return max_profit

