# Problem: D - Repeating Cipher - https://codeforces.com/gym/585107/problem/D

n=int(input())
t=input()
res=t[0]
step=2
i=0
while i+step<n:
    i+=step
    res+=t[i]
    step+=1
print(res)