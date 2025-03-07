# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_queue=deque()
        min_queue=deque()
        left=0
        res=0
        for right in range(len(nums)):
            while min_queue and nums[right]<min_queue[-1]:
                min_queue.pop()
            while max_queue and nums[right]>max_queue[-1]:
                max_queue.pop()
            min_queue.append(nums[right])
            max_queue.append(nums[right])
            while max_queue[0]-min_queue[0]>limit:
                print(max_queue[0])
                print(min_queue[0])
                if max_queue[0]==nums[left]:
                    max_queue.popleft()
                if min_queue[0]==nums[left]:
                    min_queue.popleft()
                left+=1



            res=max(res,right-left+1)
        return res

      
        