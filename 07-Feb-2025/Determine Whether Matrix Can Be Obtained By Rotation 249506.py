# Problem: Determine Whether Matrix Can Be Obtained By Rotation - https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        i=0
        while i<4:
            mat=list(zip(*mat))
            for j in range(len(mat)):
                mat[j]=list(mat[j][::-1])
            if mat==target:
                return True
            else:
                i+=1
        return False


      
