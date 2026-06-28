# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        bfs_res = []
    
        if not root:
            return bfs_res
        
        q = collections.deque([root])
        while q:
            l = []
            for _ in range(len(q)):
                curr = q.popleft()
                l.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            bfs_res.append(l)
        
        res = [k.pop() for k in bfs_res]
        return res


 
     

        