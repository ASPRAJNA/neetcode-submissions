class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        for i in range(0,len(prices)) :
            for j in range(i,len(prices)):
                if prices[j]-prices[i] > maxprofit :
                    maxprofit= prices[j]-prices[i]

        return maxprofit