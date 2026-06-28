# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)[0]
    
    def dfs(self, root):
        if not root:
            return True, 0
        
        leftIsBalanced, leftHeight = self.dfs(root.left)
        rightIsBalanced, rightHeight = self.dfs(root.right)

        if leftIsBalanced and rightIsBalanced and abs(leftHeight - rightHeight) <= 1:
            return True, max(leftHeight, rightHeight)+1
        else:
            return False, max(leftHeight, rightHeight)+1
        