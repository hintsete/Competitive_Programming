# Problem: C - Compare T-Shirt Sizes - https://codeforces.com/gym/585107/problem/C

t=int(input())

shirts=["S","M","L"]
for _ in range(t):
    
    a, b= input().split()
    pos_a=shirts.index(a[-1])
    pos_b=shirts.index(b[-1])
    if a==b:
        print("=")
    
    elif pos_a<pos_b:
        print("<")
    elif pos_a>pos_b:
        print(">")
    else:
        if pos_a==0 and pos_b==0:
            if len(a)>len(b):
                print("<")
            else:
                print(">")
        else:
            if len(a)>len(b):
                print(">")
            else:
                print("<")
    