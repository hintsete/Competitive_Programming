# Problem: D - Socialism - https://codeforces.com/gym/589822/problem/D

t = int(input())

for _ in range(t):

    n, k = map(int, input().split())

    nums = list(map(int, input().split()))
    nums.sort()
    total=sum(nums)
    max_wealth=0
    left=0
    right=len(nums)-1
    while left<= right:
        if (total/(right-left+1))>=k:
            max_wealth=right-left+1
            break
        total-=nums[left]
        left+=1
    print(max_wealth)
    