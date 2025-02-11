# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        smaller_elements=[]
        sorted_nums=sorted(nums)
        for num in nums:
            smaller_elements.append(sorted_nums.index(num))
        return smaller_elements
