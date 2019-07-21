
# 242. Valid Anagram

# My solution dictionary
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        if len(s)!=len(t): return False
        for i in s:
            if i in dic.keys():
                dic[i]+=1
            else:
                dic[i]=1
        for j in t:
            if j in dic.keys():
                dic[j]-=1
                if dic[j]<0: return False
            else:
                return False
        return True