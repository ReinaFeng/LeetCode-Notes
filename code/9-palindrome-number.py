# 9. Palindrome Number
#approach 1: Not convert to string




#My approach
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x= str(x)#int-->string
        for i in range(len(x)//2):
            if x[i]!=x[len(x)-1-i]:
                return False
        return True