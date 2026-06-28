# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = []
        self.dfs(root)
        if k <= len(self.res):
            return self.res[k-1]
        return Nonne

    
    def dfs(self, node):
        if not node:
            return
        
        self.dfs(node.left)
        self.res.append(node.val)
        self.dfs(node.right)

        