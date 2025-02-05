# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res=[]
        # using the array itself as a marker to find the duplicate
        for num in nums:
            # mapping the number with it's correct index
            index=abs(num)-1
            # if the number at that index is negative it is a duplicate
            if nums[index]<0:
                res.append(abs(num))
            # if its the first time mark the number as negative
            else:
                nums[index]=-nums[index]
                
        return res