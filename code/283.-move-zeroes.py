
#283. Move Zeroes




#My solution
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        empty = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[empty] = nums[i]
                empty += 1
        while(empty<len(nums)): # if finish filling non-zero elements, fill remaining space as 0
            nums[empty]=0
            empty +=1