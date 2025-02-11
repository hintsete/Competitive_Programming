# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left_half,right_half):
            i=0
            j=0
            sorted_array=[]
            while i<len(left_half) and j < len(right_half):
                if left_half[i]<right_half[j]:
                    sorted_array.append(left_half[i])
                    i+=1
                else: 
                    sorted_array.append(right_half[j])
                    j+=1
                
            sorted_array.extend(left_half[i:])
            sorted_array.extend(right_half[j:])

            return sorted_array
        def mergesort(left,right,nums):
            if left==right:
                return [nums[left]]
            mid=left+(right-left)//2
            left_half=mergesort(left,mid,nums)
            right_half=mergesort(mid+1,right,nums)
            return merge(left_half,right_half)
        return mergesort(0,len(nums)-1,nums)
        