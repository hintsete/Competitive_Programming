# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        output=[]
        words=s.split()
        max_len=max(len(word) for word in words)
        for i in range(max_len):
            word=""
            for w in words:
                if i<len(w):
                    word+=w[i]
                else:
                    word+=" "
                
            output.append(word.rstrip())
        return output
      