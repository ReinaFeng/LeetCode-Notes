
# 66. Plus One

# digits-->int
def plusOne(digits):
    num = 0
    for i in range(len(digits)):
    	num += digits[i] * pow(10, (len(digits)-1-i))
    return [int(i) for i in str(num+1)]



#My approach
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits)==0: return [1]
        if digits[-1]==9:
            digits = self.plusOne(digits[0:-1])
            digits.append(0)
        else:
            digits[-1]+=1
        return digits