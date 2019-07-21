
####Approach 1: Two pointers
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #keep the tail of good list(0~slow-1)
        slow = 0 
        for fast in range(len(nums)):
            #if element at fast is good, replace the next element of good list(slow)
            if(nums[fast]!=val):
                nums[slow]=nums[fast]
                slow +=1
        return slow


####Approach 2: Two pointers- When remove elements are rare
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)
        while i<n:
            if nums[i]==val:
                nums[i] = nums[n-1]
                n -=1 
                #注意这里没有i++，换过来之后继续检查原来n-1位置的数，如果还=val就再换n-2
                #直到不等于val再挪到下一位
            else:
                i +=1
        return n


####My solution
# Go through everthing and delete
# use pop
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        i = 0
        while i<length:
            if (nums[i]==val):
                nums.pop(i)
                i -=1
                length -=1
            i +=1
        return length

