# 169 majority element
# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
# You may assume that the array is non-empty and the majority element always exist in the array.

# Approach 1 Sort
class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]

# Approach 2: Boyer-Moore Voting Algorithm
class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate

# My solution: Map
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        dictionary = {}
        for i in nums:
            if i in dictionary.keys():
                dictionary[i]+=1
            else:
                dictionary[i]=1
            if  dictionary[i]>length/2: return i
        