# Problem: Love Story - https://codeforces.com/contest/1829/problem/A

t=int(input())
for _ in range(t):
    s=input()
    main_s="codeforces"
    count=0
    for i,j in zip(s,main_s):
        if i!=j:
            count+=1
        
    print(count)