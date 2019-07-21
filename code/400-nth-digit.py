# 400.Nth Digit
class Solution:
    def findNthDigit(self, n: int) -> int:
        k = 1
        th = 9
        while(th<n):
            n = n - th
            k +=1
            th = k*10**(k-1)*9
        
        #k:几位 n 第几个
        if k==1: return n
        
        a = ((n-1)//k)+1 #第几个k位数
        b = (n-1)%k+1#这个数第几位
        
        #这个数字是多少
        num = str(10**(k-1)-1 + a)
        return int(num[b-1])
        
#         #如果刚好是第一位直接求余数
#         if b==1: return ((a-1) // (10**(k-1)))+1
#         else:
#             # reutrn b-1 digits of num
#             num = (a-1) % (10**(k-1))
            
#             #第b代表倒数第k-1-b
#             if len(str(num))<k-b+1 : return 0
#             if len(str(num))<k-1: 
#                 zro = k-1-len(str(num))
#                 return int(str(num)[b-2-zro])
#             return int(str(num)[b-2])


        