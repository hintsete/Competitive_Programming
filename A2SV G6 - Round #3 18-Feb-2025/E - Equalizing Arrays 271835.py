# Problem: E - Equalizing Arrays - https://codeforces.com/gym/588468/problem/E

n=int(input())
arr1=list(map(int,input().split()))
m=int(input())
arr2=list(map(int,input().split()))

# count=[]
sum_1=0
sum_2=0
prefix_1=[]
prefix_2=[]
if sum(arr1)!=sum(arr2):
    print(-1)
    exit()
for num in arr1:
    sum_1+=num
    prefix_1.append(sum_1)
for num in arr2:
    sum_2+=num
    prefix_2.append(sum_2)
left=0
right=0
count=0
while left<len(prefix_1) and right<len(prefix_2):
    if prefix_1[left]==prefix_2[right]:
        count+=1
        left+=1
        right+=1
    elif prefix_1[left]>prefix_2[right]:
        right+=1
   
    else:
        left+=1
    
print(count if count>0 else -1)
