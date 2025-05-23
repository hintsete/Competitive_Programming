# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1_count=Counter(s1)
        window_count=Counter(s2[0:len(s1)])
        if s1_count==window_count:
            return True
        for right in range(len(s1),len(s2)):
            window_count[s2[right]]+=1
            window_count[s2[right-len(s1)]]-=1
            if window_count[s2[right-len(s1)]]==0:
                del window_count[s2[right-len(s1)]]

            if s1_count==window_count:
                return True
        return False
            
                    