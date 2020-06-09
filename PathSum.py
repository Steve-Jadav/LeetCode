# Problem 112

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return False

        if root.val == sum and root.left == None and root.right == None:
            return True

        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Approach 2: Iterative


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return False

        stack = list()
        stack.append((root, root.val))
        while stack:
            node, node_sum = stack.pop()

            if node_sum == sum and node.right == None and node.left == None:
                return True
            if node.right:
                stack.append((node.right, node.right.val + node_sum))
            if node.left:
                stack.append((node.left, node.left.val + node_sum))

        return False
