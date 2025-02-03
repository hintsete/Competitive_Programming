# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        my_list=[]
        for i,j in ranges:
           for n in range(i,j+1):
            my_list.append(n)
        for num in range(left,right+1):
            if num not in my_list:
                return False
            
        return True
      
                    