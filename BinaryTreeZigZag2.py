# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
	# Approach: Similar to level order traversal but with a flip counter.
        if (root == None):
            return []
        
        j = 0
        result = list()
        queue = list()
        queue.append(root)
        
        while queue:
            level = list()
            n = len(queue)
            
            for i in range(0, n):
                x = queue.pop(0)
                if (j % 2 == 0):
                    level.append(x.val)
                else:
                    level.insert(0, x.val)
                    
                if (x.left):
                    queue.append(x.left)
                if (x.right):
                    queue.append(x.right)
                
            result.append(level)
            j += 1
        
        return result
