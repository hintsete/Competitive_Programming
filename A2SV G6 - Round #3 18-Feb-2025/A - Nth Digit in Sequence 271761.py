# Problem: A - Nth Digit in Sequence - https://codeforces.com/gym/588468/problem/A

n=int(input())


my_strr=str(n)
my_list=[]
for i in range(1,1000):
    my_list.append(str(i))

my_strr="".join(my_list)

print(my_strr[n-1])
