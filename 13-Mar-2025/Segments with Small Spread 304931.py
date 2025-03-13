# Problem: Segments with Small Spread - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F

from collections import deque


n,k=map(int,input().split())
nums=list(map(int,input().split()))
count=0
min_stack=deque()
max_stack=deque() 
l=0
for r in range(n):
    while min_stack and nums[r]<nums[min_stack[-1]]:
        min_stack.pop()
    min_stack.append(r)
    while max_stack and nums[r]>nums[max_stack[-1]]:
        max_stack.pop()
    max_stack.append(r)
    while nums[max_stack[0]]-nums[min_stack[0]]>k:
        l+=1
        if min_stack[0]<l:
            min_stack.popleft()
        if max_stack[0]<l:
            max_stack.popleft()
    count+=r-l+1

print(count)