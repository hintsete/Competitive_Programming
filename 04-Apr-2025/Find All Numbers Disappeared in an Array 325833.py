# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
       
        disappeared=[]
        n=len(nums)
        for i in range(n):
            correct_index=abs(nums[i])-1
            while nums[correct_index]!=nums[i]:
                nums[correct_index], nums[i]=nums[i], nums[correct_index]

                correct_index=abs(nums[i])-1

            
        for i in range(n):
            if nums[i]!=i+1:
                disappeared.append(i+1)
       
            
        return disappeared