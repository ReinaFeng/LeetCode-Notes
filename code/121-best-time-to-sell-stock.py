# 121.Best Time to Buy and Sell Stock
# Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction 
# (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
# Note that you cannot sell a stock before you buy one.




#Approach 1:  dynamic programming
# class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minprice =100000000
        maxprice =0
        for i in range(len(prices)):
            if prices[i]<minprice: 
                minprice = prices[i]
            elif prices[i]-minprice>maxprice:
                maxprice = prices[i]-minprice
        return maxprice




# My approach: Dynamic 动态规划
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        new = []
        for i in range(len(prices)-1):
            new.append(prices[i+1]-prices[i])
        thisMax= 0#max in this sequence
        nowMax = 0#max in history
        for j in range(len(new)):
            thisMax = max(new[j], new[j]+thisMax,0)
            nowMax = max(thisMax,nowMax)
        return nowMax
    