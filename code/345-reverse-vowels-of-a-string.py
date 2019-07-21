# 345. Reverse Vowels of a String


# My solution: two pointers
class Solution:
    def reverseVowels(self, s: str) -> str:
        idx = "aeiouAEIOU"
        i = 0
        j = len(s)-1
        slist = list(s)
        while(i<len(s)-1 and j>0 and i<j):
            if (slist[i] in idx) and (slist[j] in idx):
                temp = slist[i]
                slist[i] = slist[j]
                slist[j] = temp
                i +=1
                j -=1
            else:
                if slist[i] not in idx:
                    i +=1
                if slist[j] not in idx:
                    j -=1
        return "".join(slist)
                