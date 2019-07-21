# 88. Merge Sorted Array

# Approach1:
def merge(self, nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0: # if nums2 left
            nums1[:n] = nums2[:n]

#My approach
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        t = -1
        while(j>-1):
            if i<0: # if nums2 left
                nums1[t] = nums2[j]
                j -= 1
                t -= 1
            elif nums1[i]>nums2[j]:
                nums1[t] = nums1[i]
                i -= 1
                t -=1
            elif nums1[i]<=nums2[j]:
                nums1[t] = nums2[j]
                j -= 1
                t -= 1
            
        return nums1
