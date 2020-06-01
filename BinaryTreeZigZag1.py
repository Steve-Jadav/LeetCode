# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
	# Approach: Using two stacks

        if (root == None):
            return []
        
        stack1 = list()
        stack2 = list()
        result = list()
        
        stack1.append(root)
        
        while (stack1 or stack2):
            
            temp = list()
            while stack1:
                x = stack1.pop()
                temp.append(x.val)
                if (x.left):
                    stack2.append(x.left)
                if (x.right):
                    stack2.append(x.right)
            
            result.append(temp)
            temp = []
            
            while stack2:
                x = stack2.pop()
                temp.append(x.val)
                if (x.right):
                    stack1.append(x.right)
                if (x.left):
                    stack1.append(x.left)
            
            if temp:
                result.append(temp)
            
        return result
