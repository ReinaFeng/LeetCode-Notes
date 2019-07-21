# 171. Excel Sheet Column Number


#My solution
class Solution:
    def titleToNumber(self, s: str) -> int:
        idx="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        s = list(s)
        output = 0
        for i in s:
            output = output*26 + idx.index(i)+1
        return output