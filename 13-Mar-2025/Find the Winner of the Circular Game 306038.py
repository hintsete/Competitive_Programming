# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:

    def findTheWinner(self, n: int, k: int) -> int:
 
        stack=[]
        for i in range(1,n+1):
            stack.append(i)
            
        def helper(stack,start):
            if len(stack)==1:
                return stack[0]
           
            remove_idx=(start+k-1)%len(stack)
            stack.pop(remove_idx)
            return helper(stack,remove_idx)
        
        return helper(stack,0)
