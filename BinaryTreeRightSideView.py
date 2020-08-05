# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Problem: 199

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        
        rightView = list()
        queue = list()
        queue.append(root)
        
        while queue:
            qLen = len(queue)
            rightView.append(queue[-1].val)
            
            for i in range(0, qLen):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return rightView
