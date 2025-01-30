# Problem: Find Three Consecutive Integers That Sum to a Given Number - https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        output=[]
        if num%3==0:
            x=num//3
            output.append(x-1)
            output.append(x)
            output.append(x+1)
        return output
