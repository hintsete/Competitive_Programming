# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

n,k=map(int,input().split())
nums=list(map(int,input().split()))
i=0
diff=[]
split=k-1
while i+1<n:
    diff.append(nums[i+1]-nums[i])
    i+=1
diff.sort(reverse=True)
largest_ksum=sum(diff[:split])
print(sum(diff)-largest_ksum)
