#67. Add Binary
# O(max(a))
class Solution:
    def addBinary(self, a, b):
        res, carry = '', 0
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0 or carry:
            curval = (i >= 0 and a[i] == '1') + (j >= 0 and b[j] == '1')
            carry, rem = divmod(curval + carry, 2)
            res = str(rem) + res
            i -= 1
            j -= 1
        return res

# recursion
#add two binary from back to front, I think it is very self explained, when 1+1 we need a carry.
   class Solution:
        def addBinary(self, a, b):
            if len(a)==0: return b
            if len(b)==0: return a
            if a[-1] == '1' and b[-1] == '1':
                return self.addBinary(self.addBinary(a[0:-1],b[0:-1]),'1')+'0'
            if a[-1] == '0' and b[-1] == '0':
                return self.addBinary(a[0:-1],b[0:-1])+'0'
            else:
                return self.addBinary(a[0:-1],b[0:-1])+'1'

# My solution:
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        output = ""
        extra = 0
        def compare(a,b):
            if len(a)>len(b):return a,b
            else: return b,a
        a, b = compare(a,b)
        i = -1
        while(i>=-len(b)):
            sum =int(a[i])+int(b[i])+extra
            if sum==0 or sum==1:
                extra = 0
                output = str(sum)+output
            else:
                extra = 1
                output = str(sum-2)+output
            i-=1
        j = -1-len(b)
        while(j>=-len(a)):
            sum = int(a[j]) + extra
            if sum==0 or sum==1:
                extra = 0
                output = str(sum)+output
            else:
                extra = 1
                output = str(sum-2)+output
            j -= 1
        output =str(extra)+output
        return str(int(output))
    
    