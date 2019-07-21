#14. Longest Common Prefix


# Approach 1
 def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        shortest = min(strs,key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest 

#My approach

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        j = 1
        if len(strs)==0: return output 
        if len(strs)==1: return strs[0]
        while(j>=0):
            for i in range(len(strs)-1):
                if j>len(strs[i]): return output
                if strs[i][:j]!=strs[i+1][:j]:
                    return output
            output = strs[0][:j]
            j +=1
        return output
    
    