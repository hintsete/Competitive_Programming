# Problem: Check if All Characters Have Equal Number of Occurrences - https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count=Counter(s)
        my_value=set()
        for value in count.values():
            my_value.add(value)
        if len(my_value)>1:
            return False
        else:
            return True
        