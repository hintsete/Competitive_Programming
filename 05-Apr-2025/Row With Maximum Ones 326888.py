# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_one=0
        idx=0
        for i, row in enumerate(mat):
            count=sum(row)
            if count>max_one:
                max_one=count
                idx=i
        return [idx,max_one]
       
        