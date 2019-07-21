# 119 Pascal's Triangle II
# Input: 3
# Output:
#   [1,3,3,1]

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        for i in range(rowIndex+1):
            row =[]
            row.append(1)
            if i==0:
                lastrow = row
                continue
            elif i==1:
                row.append(1)
                lastrow = row
                continue
            else:
                for j in range(len(lastrow)-1):
                    row.append(lastrow[j]+lastrow[j+1])
            row.append(1)
            lastrow = row
        return row
    
