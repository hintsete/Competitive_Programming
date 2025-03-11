# Problem: A - The Ticket Booth - https://codeforces.com/gym/594077/problem/A

n,s=map(int,input().split())
nums=[]
for num in range(1,n+1):
    nums.append(num)

# print(nums)
count=0
max_val=max(nums)   
if s%n==0:
    count=(s//max_val)
else:
    count=(s//max_val)+1
# else:
#     count=1
print(count)
    