# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

def x_sum(mat):
    
    # primary_dict=
    # secondary_dict=
    # for i in range(len(mat)):
    #     for j in range(len(mat[0])):
    primary_dict={}
    secomdary_dict={}
    n,m=len(mat),len(mat[0])
    for i in range(n):
        for j in range(m):
            dict1=i-j
            dict2=i+j
            primary_dict[dict1]=primary_dict.get(dict1,0)+mat[i][j]
            secomdary_dict[dict2]=secomdary_dict.get(dict2,0)+mat[i][j]
    _max=0
    for i in range(n):
        for j in range(m):
            attacked=primary_dict[i-j]+secomdary_dict[i+j]-mat[i][j]
            _max=max(_max,attacked)
    

  

    return _max












t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    matrix=[]
    for i in range(n):
        x=list(map(int,input().split()))
        matrix.append(x)
    print(x_sum(matrix))
