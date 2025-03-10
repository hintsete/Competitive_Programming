# Problem: B - Fix the Forecast! - https://codeforces.com/gym/591928/problem/B

from collections import defaultdict


t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a=[(a[i],i)for i in range(n)]
    # print(a_idx)
    a.sort()
    b.sort()
    # print(a_idx)
    # print(b)
    ans=[0]*n
    for i in range(n):
        val,idx=a[i]
        ans[idx]=b[i]
    print(*ans)


    
 
