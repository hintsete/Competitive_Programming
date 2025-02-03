# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        convert=""
        for ch in s:
            convert+=str((ord(ch)-ord("a"))+1)

     
        for i in range(k):
            _sum=0
            for num in convert:

                _sum+=int(num)
            convert=str(_sum)
        return _sum
       