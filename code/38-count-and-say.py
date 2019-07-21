# 38. Count and Say


# My solution
class Solution:
    def countAndSay(self, n: int) -> str:
        last ="1"#string on last layer
        for i in range(n-1):   #Attention
            pre =""     #accumulate string
            prechar =last[0]    # repeat character
            count = 0     #number of repeat character
            for thischar in last:
                if thischar != prechar:
                    pre = pre+str(count)+prechar    #concatenate
                    count=0
                    prechar = thischar
                if thischar==prechar:
                    count +=1
            pre = pre+str(count)+prechar
            last = pre
        return last
            