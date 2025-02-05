# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
     
        char_set=Counter(chars)
   
        res=0
        for word in words:
            word_set=Counter(word)
            valid=True

            for ch in word:
                if word_set[ch]>char_set[ch]:
                    valid=False
                    break
            if valid:
                res+=len(word)
            
        return res
