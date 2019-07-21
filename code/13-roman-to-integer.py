# 13. Roman to Integer


#Approach 1
# *Note: The trick is that the last letter is always added. 
# Except the last one, if one letter is less than its latter one, this letter is subtracted.
class Solution:
# @param {string} s
# @return {integer}
def romanToInt(self, s):
    roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
    z = 0
    for i in range(0, len(s) - 1):
        if roman[s[i]] < roman[s[i+1]]:
            z -= roman[s[i]]
        else:
            z += roman[s[i]]
    return z + roman[s[-1]]



#My solution
class Solution:
    def romanToInt(self, s: str) -> int:
        dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        output = 0
        i=0
        while(i<len(s)):
            if s[i:i+2] in dic.keys():
                output += dic[s[i:i+2]]
                i +=2
                continue
            else:
                output += dic[s[i]]
                i +=1
        return output
            