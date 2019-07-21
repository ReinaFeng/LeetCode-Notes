# 125. Valid Palindrome


# My solution: Two pointers
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while(i<j):
            if s[i].isalnum()==False:
                i +=1
                continue
            if s[j].isalnum()==False:
                j -=1
                continue
            if s[i].lower()!=s[j].lower():
                return False
            i+=1
            j-=1
        return True