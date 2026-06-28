# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, float('-inf'), float('inf'))

    def dfs(self, root, low, high):
        if not root:
            return True
        
        if root.val <= low or root.val >= high:
            return False
        
        left_isBST = self.dfs(root.left, low, root.val)
        right_isBST = self.dfs(root.right, root.val, high)
        if left_isBST and right_isBST:
            return True
        return False
        