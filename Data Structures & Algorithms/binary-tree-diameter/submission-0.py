# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.getHeight(root)
        return self.diameter

    def getHeight(self, node):
        if not node:
            return 0

        leftHeight = self.getHeight(node.left)
        rightHeight = self.getHeight(node.right)

        longest_path_of_node = leftHeight + rightHeight
        self.diameter = max(self.diameter, longest_path_of_node)

        return max(leftHeight, rightHeight) + 1


        