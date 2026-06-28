# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, root.val)
    
    def dfs(self, node, maxValue):
        if not node:
            return 0
        
        res = 1 if node.val >= maxValue else 0
        maxValue = max(node.val, maxValue)
        res += self.dfs(node.left, maxValue)
        res += self.dfs(node.right, maxValue)
        
        return res
        