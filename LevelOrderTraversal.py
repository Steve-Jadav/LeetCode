# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if root is None:
            return None
        
        result = [[root.val]]
        queue = [root]
        
        while (queue):
            next_level = list()
            n = len(queue)
            for i in range(0, n):
                x = queue.pop(0)
                if x.left:
                    queue.append(x.left)
                    next_level.append(x.left.val)
                if x.right:
                    queue.append(x.right)
                    next_level.append(x.right.val)
            
            if (len(next_level) != 0):
                result.append(next_level)
        
        return result
