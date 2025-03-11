# Problem: E - From S To T - https://codeforces.com/gym/585107/problem/E

from collections import Counter


q=int(input())
for i in range(q):
    s=input().lower()
    t=input().lower()
    p=input().lower()

    s_idx=0
    t_idx=0
    while s_idx<len(s) and t_idx<len(t):
        if t[t_idx]==s[s_idx]:
            s_idx+=1
        t_idx+=1
    if s_idx<len(s):
        print("NO")
        continue
    count_s=Counter(s)
    count_t=Counter(t)
    count_p=Counter(p)
    valid=True
    for keys in count_t:
        n=count_t[keys]
        a=count_s.get(keys,0)+count_p.get(keys,0)
        if n > a:
            valid=False
            break
    print("YES" if valid else "NO")
