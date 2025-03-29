# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def valid(mid):
            total_car=0
            for rank in ranks:
                total_car+=int(math.sqrt(mid//rank))
            print(total_car)
            return total_car>=cars


        l=1
        r=max(ranks)*(cars*cars)
        while l<=r:
            mid=(l+r)//2
            if valid(mid):
                r=mid-1
            else:
                l=mid+1
        return l