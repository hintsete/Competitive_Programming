# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

from itertools import accumulate
t=int(input())
for _ in range(t):
    n=int(input())
    red=list(map(int,input().split()))
    m=int(input())
    blue=list(map(int,input().split()))
    prefix_r=[0]+list(accumulate(red))
    prefix_b=[0]+list(accumulate(blue))
    print(max(prefix_b)+max(prefix_r))