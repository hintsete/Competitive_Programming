# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i=0
        while i+1<len(nums):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
            i+=1
        # return nums[]
        ans=[]
        # for num in nums:
        #     if num!=0:
        #         ans[0]=num
        c=0
        for i in range(len(nums)):
            if nums[i]!=0:
                ans.append(nums[i])
            else:
                c+=1

            
            
        return ans+[0]*c
                

        