# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        max_heap=[]
        for pile in piles:
            max_heap.append(-pile)
        heapq.heapify(max_heap)
        for _ in range(k):
            large=-(heapq.heappop(max_heap))
            reduced=large-(large//2)
            heapq.heappush(max_heap,-reduced)
        return -(sum(max_heap))

        