# Problem: Longest Nice Substring - https://leetcode.com/problems/longest-nice-substring/

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def div(s):
            if len(s)<=1:
                return ""

            seen=set(s)
            for idx, char in enumerate(s):
                opposite_chr=char.swapcase()
                if opposite_chr not in seen:
                    left=div(s[:idx])
                    right=div(s[idx+1:])
                    if len(left)>=len(right):
                        return left

                    else:
                        return right
            return s

               
        return div(s)
