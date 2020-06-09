# Problem 129.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if root == None:
            return 0

        total = self.getSum(root, 0)
        return total

    def getSum(self, root, t):
        if root == None:
            return 0

        t = (t * 10) + root.val

        if root.left == None and root.right == None:
            return t

        return self.getSum(root.left, t) + self.getSum(root.right, t)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# APPROACH 2:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def __init__(self):
        self.path_sum = 0

    def sumNumbers(self, root: TreeNode) -> int:
        if root == None:
            return 0

        path = str(root.val)
        self.sum_utility(root, path)
        return self.path_sum

    def sum_utility(self, node, path):

        if node.left == None and node.right == None:
            self.path_sum += int(path)
            return

        if node.left:
            self.sum_utility(node.left, path + str(node.left.val))

        if node.right:
            self.sum_utility(node.right, path + str(node.right.val))
