# Problem: A - Kibr and His Musics - https://codeforces.com/gym/589822/problem/A

from itertools import accumulate


n, m=map(int,input().split())
new_arr=[]
for _ in range(n):
    c, t=map(int,input().split())
    # print(c)
    # print(t)
    new_arr.append((c*t))
# print(new_arr)
new_arr=list(accumulate(new_arr))
# print(new_arr)
moments=list(map(int,input().split()))
pointer=0
count=1
for i in range(m):
    # count+=1
    while pointer<n and  moments[i]>new_arr[pointer]:
        pointer+=1
        count+=1
    # if pointer<n and moments[i]<=new_arr[pointer]:
    #     count+=1
    print(count)