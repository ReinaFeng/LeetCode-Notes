# 344. Reverse String

class Solution(object):
    def reverseString(self, s):
        l = len(s)
        if l < 2:
            return s
        return self.reverseString(s[l/2:]) + self.reverseString(s[:l/2])


class SolutionClassic(object):
    def reverseString(self, s):
        r = list(s)
        i, j  = 0, len(r) - 1
        while i < j:
            r[i], r[j] = r[j], r[i]
            i += 1
            j -= 1

        return "".join(r)

class SolutionPythonic(object):
    def reverseString(self, s):
        return s[::-1]

#My approachs
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(int(len(s)/2)):
            a= s[i]
            s[i]=s[-i-1]
            s[-i-1] = a