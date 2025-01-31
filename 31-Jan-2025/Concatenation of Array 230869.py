# Problem: Concatenation of Array - https://leetcode.com/problems/concatenation-of-array/description/

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=nums[:]
        for item in nums:
            ans.append(item)
        return ans