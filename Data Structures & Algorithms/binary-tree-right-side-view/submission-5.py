# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
    
        if not root:
            return res
        
        q = collections.deque([root])
        while q:
            size_q = len(q)
            for i in range(len(q)):
                curr = q.popleft()
                if i == size_q - 1:
                    res.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        
        return res


 
     

        