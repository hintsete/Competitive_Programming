# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        coin=0
        piles.sort()
        n=[]
        i=0
      
        l=0
        for pile in piles[len(piles)//3:]:
            
            if l%2==0:
                coin+=pile
            l+=1
        return coin
