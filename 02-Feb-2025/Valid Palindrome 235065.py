# Problem: Valid Palindrome - https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s_alnum="".join(char for char in s if char.isalnum())
        if s_alnum[:]==s_alnum[::-1]:
            return True
        else:
            return False
        