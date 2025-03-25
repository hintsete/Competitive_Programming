# Problem: C - The Splitting Game - https://codeforces.com/gym/586960/problem/C

from collections import Counter


t=int(input())
for _ in range(t):
    n=int(input())
    s=input().lower()
    right=Counter(s)
    left=Counter()
    max_sum=0
    for ch in s:
        right[ch]-=1
        left[ch]+=1
        if right[ch]==0:
            del right[ch]
        length=len(right)+len(left)
        max_sum=max(max_sum,length)
    print(max_sum)