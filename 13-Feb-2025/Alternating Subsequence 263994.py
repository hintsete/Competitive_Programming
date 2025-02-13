# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

t=int(input())
for _ in range(t):
    n=int(input())
    nums=list(map(int,input().split()))
   
    i=0
    max_sum=0
    # for i in range(len(nums)):
    while i<n:
        max_val=nums[i]
        while i+1<n and nums[i]*nums[i+1]>0:
            max_val=max(max_val,nums[i+1])
            i+=1
        max_sum+=max_val
        i+=1
        
   
        
      
    print(max_sum)
