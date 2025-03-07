# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

t=int(input())
for _ in range(t):
    n=int(input())
    nums=list(map(int,input().split()))
    nums_new=sorted(nums)
    if nums==nums_new:
        print(0)
        continue
    i=0
    count=0
    while i<n:
        j=i+1
        if j<n and  nums[i]>nums[j]:
            count+=1
            i=j+1
        else:
            i+=1
    print(count)
