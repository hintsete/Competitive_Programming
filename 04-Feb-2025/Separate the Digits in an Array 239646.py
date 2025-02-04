# Problem: Separate the Digits in an Array - https://leetcode.com/problems/separate-the-digits-in-an-array/description/

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        joined="".join(map(str,nums))
        answer=[]
        for num in joined:
            answer.append(int(num))
        return answer
      
    