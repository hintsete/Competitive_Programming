# Problem: Books - https://codeforces.com/contest/279/problem/B

n, t=map(int,input().split())
nums=list(map(int,input().split()))
left=0
book=0
count=0
for right in range(n):
    book+=nums[right]
    while book>t:
        book-=nums[left]
        left+=1
    count=max(count,right-left+1)
print(count)