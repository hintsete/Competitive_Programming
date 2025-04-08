# Problem: Limited Repainting - https://codeforces.com/contest/2070/problem/C

t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    s=input()
    penality=list(map(int,input().split()))
    def valid(mid):
        count=0
        seg=False
        for i in range(len(penality)):
            if penality[i]<=mid:
                continue
            
            if s[i]=="B":
                if not seg:
                    count+=1
                    seg=True
                
            else:
                seg=False
        return count<=k


        

    l=0
    r=max(penality)
    ans=r
    while l<=r:
        mid=(l+r)//2
        if valid(mid):
            ans=mid
            r=mid-1
        else:
            l=mid+1
    print(ans)
    
            