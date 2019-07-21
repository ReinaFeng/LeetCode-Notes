# 53. Maximum Subarray
# Approach 1：
for i in range(1, len(nums)):
        if nums[i-1] > 0:
            nums[i] += nums[i-1]
    return max(nums)

#Approach2:  Divide and conquer
class Solution:
    # @param {integer[]} nums
    # @return {integer}
     

     def maxSubArrayHelper(self,nums, l, r):
        if l > r:
            return -2147483647
        m = (l+r) / 2
        
        leftMax = sumNum = 0
        for i in range(m - 1, l - 1, -1):
            sumNum += nums[i]
            leftMax = max(leftMax, sumNum)
        
        rightMax = sumNum = 0
        for i in range(m + 1, r + 1):
            sumNum += nums[i]
            rightMax = max(rightMax, sumNum)
            
        leftAns = self.maxSubArrayHelper(nums, l, m - 1)
        rightAns = self.maxSubArrayHelper(nums, m + 1, r)
            
        return max(leftMax + nums[m] + rightMax, max(leftAns, rightAns))
        
     def maxSubArray(self, nums):
        return self.maxSubArrayHelper(nums, 0, len(nums) - 1)




#My approach:
#O(n),O(1)
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        historymax = nums[0]
        thismax = 0
        for i in range(len(nums)):
            thismax = max(nums[i],nums[i]+thismax)
            historymax = max(thismax, historymax)
        return historymax
    