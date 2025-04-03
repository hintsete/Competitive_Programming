# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=defaultdict(int)
        frequency=[[] for _ in range(len(nums)+1)]
        for n in nums:
            count[n]+=1
        # c is the number of counts used as an index in frequency 2d list and n is the list of values with that number of occurence
        for n,c in count.items():
            frequency[c].append(n)

        print(frequency)

        # now iterate through frequency in reverse order to pop the frequently occured number
        res=[]
        
        for i in range(len(frequency)-1,0,-1):
            for n in frequency[i]:
                res.append(n)
                while len(res)==k:
                    return res
                
            