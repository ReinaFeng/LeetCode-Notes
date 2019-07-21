
# 172. Factorial Trailing Zeroes
class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0 
        x = n
        out = 0
        while (x>=5):
            count +=1 #log5(n)
            x //= 5
            out += n//(5**count)# n//5 + n//25 + n//125...
        return out
    