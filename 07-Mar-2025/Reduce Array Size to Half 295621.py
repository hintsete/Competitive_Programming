# Problem: Reduce Array Size to Half - https://leetcode.com/problems/reduce-array-size-to-the-half/

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count=Counter(arr)
        half=len(arr)//2
        value=[]
        
        for idx,val in count.items():
            value.append(val)
        value.sort(reverse=True)
        prefix=list(accumulate(value))
        print(value)
        print(prefix)
        i=0
        c=0
        while i<len(arr):
            if prefix[i]>=half:
               
                c+=1
                break

            i+=1
            c+=1
        return c
       
        