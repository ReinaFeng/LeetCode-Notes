#189 Rotate Array
#Given an array, rotate the array to the right by k steps, where k is non-negative.
#Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
#Could you do it in-place with O(1) extra space?

# Approach 1: Cyclic replacement

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        count = 0
        start = 0
        while count < len(nums):
            current = start 
            prev = nums[start] #store the value in the position
            
            while True:
                next = (current + k) % len(nums) #
                temp = nums[next] #store it temporaly 
                nums[next] = prev #overide the next 
                prev = temp #reset prev
                current = next #reset current
                count += 1
                
                if start == current:
                    break 
            start += 1

# Approach 2: Reverse
class Solution(object):
    
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        self.reverse(nums,0,len(nums)-1)
        self.reverse(nums,0, k-1)
        self.reverse(nums,k, len(nums)-1)

    def reverse(self, nums, start, end):
        """
        :type nums: List[int]
        :type start: int
        :type end: int
        :rtype: None
        """
        while start < end: #
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp 
            start += 1
            end -= 1
   









# My solution1 # Extra Array
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        saveK=[]
        step = length-(k%length)# deal with the case that k>length
        for i in range(length+step):
            if i<step:
                saveK.append(nums[i])
            elif i<length:
                nums[i-step]=nums[i]
            else:
                nums[i-step]=saveK[i-length]