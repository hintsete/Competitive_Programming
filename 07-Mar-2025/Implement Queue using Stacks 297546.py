# Problem: Implement Queue using Stacks - https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.enqueue=[]
        self.dequeue=[]
        

    def push(self, x: int) -> None:
        self.enqueue.append(x)
        # self.dequeue.append(x)

        

    def pop(self) -> int:
        # print(self.dequeue.reverse())
        if not self.dequeue:
            while self.enqueue:
                self.dequeue.append(self.enqueue.pop())
        return self.dequeue.pop() if self.dequeue else -1
        

    def peek(self) -> int:
        # while self.dequeue:
        #     return self.dequeue.reverse()[-1]
        # else:
        #     return 0
        # print(0)
        if not self.dequeue:
            while self.enqueue:
                self.dequeue.append(self.enqueue.pop())
        return self.dequeue[-1] if self.dequeue else -1
        

    def empty(self) -> bool:
        return not self.dequeue and not self.enqueue
        # print(True)
