# Problem: H-Index II - https://leetcode.com/problems/h-index-ii/description/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
     
        l=0
        r=len(citations)-1
        while l<=r:
            mid=(l+r)//2
            paper=len(citations)-mid
            if citations[mid]==paper:
                return paper
            elif citations[mid]>paper:
                r=mid-1

            else:
                l=mid+1
          
                
        return len(citations)-l
