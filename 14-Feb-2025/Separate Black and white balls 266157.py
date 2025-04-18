# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        # right=len(s)-1
        count=0
        ans=0
        for right in range(len(s)-1,-1,-1):
            if s[right]=="":
                count+=ans
            else:
                ans+=1

        return count