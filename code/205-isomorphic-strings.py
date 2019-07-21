#205. Isomorphic Strings

#My solution
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}
        for i in range(len(s)):
            if s[i] in dic.keys():
                if dic[s[i]]!=t[i]:
                    return False
            else:
                if t[i] in dic.values():#avoid aa-ab
                    return False
                dic[s[i]]=t[i]
        return True