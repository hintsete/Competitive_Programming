# Problem: Find Consecutive Integers from a Data Stream - https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream:

    def __init__(self, value: int, k: int):
        self.stream=deque()
        self.k=k
        self.value=value
        self.count=0
        

    def consec(self, num: int) -> bool:

        self.stream.append(num)
        if num==self.value:
            self.count+=1
        # else:
        #     self.count=0
        if len(self.stream)>self.k:
            left=self.stream.popleft()
            if left==self.value:
                self.count-=1
        return self.count==self.k