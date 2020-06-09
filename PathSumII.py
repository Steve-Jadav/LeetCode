# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root == None:
            return []
        
        paths = list()
        stack = list()
        stack.append((root, root.val, [root.val]))
        
        while stack:
            node, node_sum, current_path = stack.pop()
            
            if node_sum == sum and node.right == None and node.left == None:
                paths.append(current_path)
            
            if node.right:
                stack.append((node.right, node_sum + node.right.val, current_path + [node.right.val]))
            if node.left:
                stack.append((node.left, node_sum + node.left.val, current_path + [node.left.val]))
                
        return paths
