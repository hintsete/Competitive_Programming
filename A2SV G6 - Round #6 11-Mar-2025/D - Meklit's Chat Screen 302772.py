# Problem: D - Meklit's Chat Screen - https://codeforces.com/gym/594077/problem/D

from collections import defaultdict, deque


n, k=map(int,input().split())
ids=list(map(int,input().split()))

chat=set()
queue=deque()
for id in ids:
    if id not in chat:
        if len(chat)==k:
            removed=queue.pop()
            chat.remove(removed)
        queue.appendleft(id)
        chat.add(id)


    
   

    
print(len(queue))
print(*queue)