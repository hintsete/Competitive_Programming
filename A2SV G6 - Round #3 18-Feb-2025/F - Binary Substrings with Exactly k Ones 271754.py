# Problem: F - Binary Substrings with Exactly k Ones - https://codeforces.com/gym/588468/problem/F

k=int(input())
s=input()
# left=0
nums=[]
for ch in s:
    nums.append(int(ch))
# print(nums)

def calculator(x):
    if x<0:
        return 0
    left=0
    current_sum=0
    res=0
    for right in range(len(nums)):
        current_sum+=nums[right]
        while current_sum>x:
            current_sum-=nums[left]
            left+=1
        res+=(right-left+1)
    return res
ans=calculator(k)-calculator(k-1)
# print(calculator(k),calculator(k-1))
print(ans)

