# Problem: Largest Number - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums=list(map(str,nums))
        print(nums)
      
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if nums[j]+nums[j+1]<nums[j+1]+nums[j]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
                
            
        print(nums)

        return str(int("".join(nums)))