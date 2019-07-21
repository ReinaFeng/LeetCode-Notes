#58. Length of Last Word


#Approach 1
class Solution:
    def lengthOfLastWord(self, s):
        cnt = 0#save count of last nonspace character
        for v in reversed(s):
            if v.isspace():
                if cnt: break #if !=0, return count
            else: cnt += 1
        return cnt


#My approach
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s)==0: return 0
        nonspace = 0
        space = 0
        for i in range(len(s)-1,-1,-1):
            if s[i]==" ":
                if nonspace==0:
                    space+=1
                    continue
                else:
                    return len(s)-i-1-space
            else:
                nonspace+=1
        if nonspace!=0: return len(s)-space
        else: return 0
# modified my answer
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        nonspace = 0
        for i in range(len(s)-1,-1,-1):
            if s[i]==" ":
                if nonspace==0:
                    continue
                else:
                    return nonspace
            else:
                nonspace+=1
        if nonspace!=0: return nonspace
        return 0
        