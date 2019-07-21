# 217. Contains Duplicate
# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array, 
# and it should return false if every element is distinct.

# Approach 1: Sort

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for i in range(len(nums)-1):#注意边缘
            if nums[i]==nums[i+1]: return True
        return False

# Approach 2： Hash Set

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic =set()
        for i in nums:
            if i in dic:
                return True
            else:
                dic.add(i)
        return False