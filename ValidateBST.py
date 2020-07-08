# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Approach: Inorder Traversal of a BST is always sorted.

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root == None:
            return True

        x = float("-inf")
        stack = list()
        current = root

        while True:
            if current:
                stack.append(current)
                current = current.left

            elif stack:
                current = stack.pop()
                if current.val <= x:
                    return False
                x = current.val
                current = current.right

            else:
                break

        return True
