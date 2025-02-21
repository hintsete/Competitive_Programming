# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/


class LRUCache:
    def __init__(self, capacity: int):
        self.recent = []
        self.elements = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.elements:
            return -1
        
        self.recent.remove(key)
        self.recent.append(key)
          
        return self.elements[key]

    def put(self, key: int, value: int) -> None:
        if key in self.elements:
            self.elements[key] = value
            self.recent.remove(key)
            
        else:
            if self.capacity == len(self.elements):
                deleted = self.recent[0]
                self.recent.pop(0)
                self.elements.pop(deleted)
            
            self.elements[key] = value
             
        self.recent.append(key)
        