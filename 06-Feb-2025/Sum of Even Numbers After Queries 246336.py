# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        total=0
        output=[]
        for num in nums:
            if num%2==0:
                total+=num
            
        for val,index in queries:
            if nums[index]%2==0:
                total-=nums[index]
            nums[index]+=val
            if nums[index]%2==0:
                total+=nums[index]
            output.append(total)
        return output