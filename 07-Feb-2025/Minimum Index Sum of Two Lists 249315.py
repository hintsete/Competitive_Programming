# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
      
            
        n=len(list1)
        m=len(list2)
        min_index=2000
        res=[]
        for i in range(n):
            for j in range(m):
                if list1[i]==list2[j]:
                    least=i+j
                    if least< min_index:
                        res=[list1[i]]
                        min_index=min(least,min_index)
                    elif least==min_index:
                        res.append(list1[i])
        return res

        