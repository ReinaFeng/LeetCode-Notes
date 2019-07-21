
# 231. Power of Two
# My approach
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        m = 1
        while(m<n):
            m *=2
        if m==n: return True
        else: return False




# Bit operation
return n > 0 && ((n & (n-1)) == 0);
# Bit count
return n > 0 && Integer.bitCount(n) == 1;