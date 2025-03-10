# Problem: Maximize Happiness of Selected Children - https://leetcode.com/problems/maximize-happiness-of-selected-children/?envType=daily-question&envId=2024-05-09

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        res=0
        happiness.sort()
        for i in range(k):
            happy=happiness.pop()
            if happy-i<0:
                break
            else:
                res+=happy-i

            print(happy)
            print(res)
        return res
        