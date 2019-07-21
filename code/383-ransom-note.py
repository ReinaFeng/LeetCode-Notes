#383. Ransom Note



#Approach 1
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for i in set(ransomNote):
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True



#My approach
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = {}
        for m in magazine:
            if m in dic.keys():
                dic[m]+=1
            else:
                dic[m]=1
        for r in ransomNote:
            if r in dic.keys():
                dic[r] -=1
                if dic[r]<0:
                    return False
            else:
                return False
        return True