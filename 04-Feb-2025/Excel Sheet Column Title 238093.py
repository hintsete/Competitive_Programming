# Problem: Excel Sheet Column Title - https://leetcode.com/problems/excel-sheet-column-title/description/?envType=problem-list-v2&envId=string

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result=[]
        while columnNumber>0:
            num=(columnNumber-1)%26
            ch=chr(ord("A")+num)
            result.append(ch)
            columnNumber=(columnNumber-1)//26
            new_result="".join(result)
        return new_result[::-1]
