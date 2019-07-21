#387. First Unique Character in a String
#Three ways
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        for i in range(len(s)):
            c = s[i]
            if s.count(c)==1:
                return i

        return -1

    def firstUniqChar2(self, s):

        from collections import Counter
        sc = Counter(s)
        for i in range(len(s)):
            c = s[i]
            if sc.get(c,0)==1:
                return i

        return -1

    def firstUniqChar3(self, s):

        d = {}
        for c in s:
            if c in d.keys():
                d[c] += 1
            else:
                d[c] = 1

        for i in range(len(s)):
            c = s[i]
            if d[c]==1:
                return i

        return -1 


#My approach
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic ={}
        idx ={}
        for i in range(len(s)):
            if s[i] in dic.keys():
                dic[s[i]]+=1
            else: 
                dic[s[i]] = 1
                idx[s[i]] = i
        for j in dic.keys():
            if dic[j]==1:
                return idx[j]
        return -1