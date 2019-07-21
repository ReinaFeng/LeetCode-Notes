#### Approach 1: Two pointers

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0: return 0; #注意数据长度为0的特例
        slow = 1
        cur_val = nums[0]
        for elem in nums:
            if(elem!=cur_val):
                nums[slow]=elem
                cur_val = elem
                slow +=1
        return slow

        