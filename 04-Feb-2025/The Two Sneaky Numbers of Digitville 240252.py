# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        res=[]
        for key,value in count.items():
            if value==2:
                res.append(key)
        return res
        