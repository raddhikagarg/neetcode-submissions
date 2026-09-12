
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        l = len(prices)
        for i in range (0,l-1):
            for j in range (i+1, l):
                if prof < prices[j] - prices[i]:
                    prof = prices[j] - prices[i]
        return prof
        

        
        