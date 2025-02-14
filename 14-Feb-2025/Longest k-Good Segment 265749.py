# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

n, k=map(int,input().split())
nums=list(map(int,input().split()))
left=0
window={}
sub_s=[0,0]
distinct_count=0
for right in range(n):
    window[nums[right]]=window.get(nums[right],0)+1
    while len(window)>k and left<n:
        window[nums[left]]-=1
        if window[nums[left]]==0:
            del window[nums[left]]
        left+=1
    if right-left>sub_s[1]-sub_s[0]:
        sub_s=[left,right]
    
print(sub_s[0]+1,sub_s[1]+1)