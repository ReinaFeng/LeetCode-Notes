#258. Add Digits




#aproach 1: loop
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while(num >= 10):
            temp = 0
            while(num > 0):
                temp += num % 10
                num /= 10
            num = temp
        return num

#approach2: np loop/recursion====> digital root
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0 : return 0
        else:return (num - 1) % 9 + 1




#My solution: recursion
class Solution:
    def addDigits(self, num: int) -> int:
        print(num)
        while self.sumDigits(num)>=10:  #self
            num = self.sumDigits(num)
        return self.sumDigits(num)
    def sumDigits(self,num):    #self
        sum = 0
        while(num>0):
            sum += num%10
            num = num//10
        return sum