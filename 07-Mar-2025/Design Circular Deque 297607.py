# Problem: Design Circular Deque - https://leetcode.com/problems/design-circular-deque/

class MyCircularDeque:

    def __init__(self, k: int):
        self.dequeue=[]
        self.k=k
        

    def insertFront(self, value: int) -> bool:
        if len(self.dequeue)<self.k:
            self.dequeue.insert(0,value)
            return True
        return False
           
            
        

    def insertLast(self, value: int) -> bool:
        if len(self.dequeue)<self.k:
            self.dequeue.append(value)
            return True
        return False
           
        
        

    def deleteFront(self) -> bool:
        if self.dequeue:
            self.dequeue.pop(0)
            return True
        return False
      
        

    def deleteLast(self) -> bool:
        if self.dequeue:
            self.dequeue.pop()
            return True
        return False
      
        
        

    def getFront(self) -> int:
        while self.dequeue:
           return self.dequeue[0]
        else:
            return -1
        

        

    def getRear(self) -> int:
        while self.dequeue:
            return self.dequeue[-1]
        else:
            return -1
      
        

    def isEmpty(self) -> bool:
        return not self.dequeue 
        

    def isFull(self) -> bool:
        return len(self.dequeue)==self.k 