# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = list()
        
        if root is None:
            return result
    
        queue = [root]
        
        while (queue):
            level = list()
            n = len(queue)
            for i in range(0, n):
                x = queue.pop(0)
                level.append(x.val)
                if x.left:
                    queue.append(x.left)
                if x.right:
                    queue.append(x.right)
            
            result.append(level)
        
        return result
