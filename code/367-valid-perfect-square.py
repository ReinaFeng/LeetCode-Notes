#367. Valid Perfect Square


#My appraoch
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        #binary search
        if num==1: return True
        low = 0
        high = num
        mid = num//2
        while(mid>1):
            if mid*mid>num:
                high = mid
            elif mid*mid<num:
                low = mid
            else:
                return  True
            if (high-low == 1): return False
            mid = (low+high)//2
        return False