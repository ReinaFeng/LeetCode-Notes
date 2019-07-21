
# 20. Valid Parentheses

#My approach: stack
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic={')':'(',']':'[','}':'{'}
        for i in s:
            if i=='(' or i=='[' or i=='{':
                stack.append(i)
            else:
                if len(stack)==0 or stack[-1]!=dic[i]:  #'}' or '(]'
                    return False
                else:
                    stack.pop(-1)
        if len(stack)!=0:return False   #'('
        return True #'' or '()'
        #  return stack == []