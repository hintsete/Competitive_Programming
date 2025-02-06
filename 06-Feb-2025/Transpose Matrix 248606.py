# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        output=[]
        for i in range(len(matrix[0])):
            arr=[]
            for j in range(len(matrix)):
                arr.append(matrix[j][i])
            output.append(arr)
        return output