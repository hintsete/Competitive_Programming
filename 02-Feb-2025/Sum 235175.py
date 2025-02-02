# Problem: Sum - https://codeforces.com/contest/1742/problem/A

t=int(input())
for _ in range(t):
    a, b, c =map(int,input().split())
    if a==abs(c-b) or b==abs(c-a) or c==abs(b-a):
        print("YES")
    else:
        print("NO")