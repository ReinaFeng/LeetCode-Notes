#122. Best Time to Buy and Sell Stock II
# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like 
# (i.e., buy one and sell one share of the stock multiple times).
# Note: You may not engage in multiple transactions at the same time 
# (i.e., you must sell the stock before you buy again).


# Approach 1 
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxprofit = 0
        for i in range(len(prices)-1):
            if prices[i+1]>prices[i]:
                maxprofit += prices[i+1]-prices[i]
        return maxprofit
                
# Approach 2 : valley&peak
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        peak = 0
        if len(prices)==0: return 0
        maxprofit = 0
        for i in range(len(prices)-1):
            valley = prices[i]
            if prices[i+1]<=prices[i]:
                valley = prices[i+1]
            if prices[i+1]>=prices[i]:
                peak = prices[i+1]
                maxprofit += peak-valley
            
        return maxprofit
            
          

# My approach
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sumprofit = 0
        maxprofit = 0
        minprice = 100000
        for i in range(len(prices)):
            if i>0:
                if prices[i]<prices[i-1]:
                    sumprofit += maxprofit
                    maxprofit = 0
                    minprice = prices[i]
            if prices[i]<minprice:
                minprice = prices[i]
            elif prices[i]-minprice>maxprofit:
                maxprofit = prices[i]-minprice
        sumprofit += maxprofit
        return sumprofit
                
        