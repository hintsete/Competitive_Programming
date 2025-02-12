# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex={} 
        # map each unique char to the last index in s
        for i,c in enumerate(s):
            lastIndex[c]=i
        output=[]
        size,end=0,0 # to track the size and end-index of each partition
        for i,c in enumerate(s):
            size+=1
            end=max(end,lastIndex[c])

            #checks if the current index i is equal to the end-index to stop the partition and hop to the next one
            if i==end:
                output.append(size)
                size=0
            

        return output