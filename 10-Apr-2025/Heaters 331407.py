# Problem: Heaters - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
       
        max_val=0
        for house in houses:
            l=0
            r=len(heaters)
            while l<r:
                mid=(l+r)//2
                
                if heaters[mid]<=house:
                    l=mid+1

                else:
                    r=mid
            min_distance=float("inf")
            if l<len(heaters):
                min_distance=abs(house-heaters[l])

            if l>0:
                min_distance=min(min_distance,abs(house-heaters[l-1]))
            max_val=max(max_val,min_distance)
        
        return max_val