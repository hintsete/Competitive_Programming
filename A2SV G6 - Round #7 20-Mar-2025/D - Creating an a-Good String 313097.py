# Problem: D - Creating an a-Good String - https://codeforces.com/gym/596141/problem/D

def solve(l,r,c,s):
    if l==r:
        if s[l]==c:
            return 0
        else:
            return 1
    mid=(r+l)//2
    left_change=(mid-l+1)-s[l:mid+1].count(c)
    next_chr=chr(ord(c)+1) if c!="z" else c
    left_result=left_change+solve(mid+1,r,next_chr,s)
    right_change=r-mid-s[mid+1:r+1].count(c)
    next_chr=chr(ord(c)+1) if c!="z" else c
    right_result=right_change+solve(l,mid,next_chr,s)
    return min(left_result,right_result)

    



t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    print(solve(0,len(s)-1,"a",s))
