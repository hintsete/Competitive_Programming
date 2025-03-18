# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        maxDiff=0
        def dfs(node,curr_min,curr_max):
            nonlocal maxDiff
            if not node:
                return 0
            dfs_min=abs(node.val-curr_min)
            dfs_max=abs(node.val-curr_max)
            maxDiff=max(maxDiff,dfs_min,dfs_max)
            curr_min=min(curr_min,node.val)
            curr_max=max(curr_max,node.val)
            dfs(node.left,curr_min,curr_max)
            dfs(node.right,curr_min,curr_max)
        dfs(root,root.val,root.val)
        return maxDiff