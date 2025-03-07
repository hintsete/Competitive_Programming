# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

from itertools import accumulate


n=int(input())
costs=list(map(int,input().split()))
costs_pre=[0]+list(accumulate(costs))
sorted_cost=sorted(costs)
sorted_cost_pre=[0]+list(accumulate(sorted_cost))
# print(sorted_cost_pre)
# print(costs_pre)
m=int(input())
for _ in range(m):
    type,l,r=map(int,input().split())
    
    if type==1:
        # print(costs_pre[r]-costs_pre[l-1])
        print(costs_pre[r]-costs_pre[l-1])
    elif type==2:
        print(sorted_cost_pre[r]-sorted_cost_pre[l-1])

