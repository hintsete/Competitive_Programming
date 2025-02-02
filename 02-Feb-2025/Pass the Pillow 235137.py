# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/description/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
       no_hops=n-1
       no_round=time//no_hops
       res=0
       if no_round%2==0:
        res=1+(time%no_hops)
       else:
         res=(n-time%no_hops)
       return res
            
        