# Pascal's Triangle
# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        List = []
        for i in range(numRows):
            row =[]
            row.append(1)
            if i==0:
                List.append(row)
                continue
            elif i==1:
                row.append(1)
                List.append(row)
                continue
            else:
                for j in range(len(List[i-1])-1):
                    row.append(List[i-1][j]+List[i-1][j+1])
            row.append(1)
            List.append(row)
        return List
                