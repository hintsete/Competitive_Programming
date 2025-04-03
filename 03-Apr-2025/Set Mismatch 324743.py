# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)

        mismatch=[0,0]  
     
        count=Counter(nums)
        for i in range(1,n+1): 
            if count[i]==0:
                mismatch[1]+=i
            if count[i]==2:
                mismatch[0]+=i
            
        return mismatch