"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root == None:
            return []

        traversal = list()
        stack = list()
        stack.append(root)

        while stack:
            current = stack.pop()
            traversal.append(current.val)
            for i in range(len(current.children) - 1, -1, -1):
                stack.append(current.children[i])

        return traversal


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Approach 2: Recursive

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root == None:
            return []

        result = [root.val]
        result += self.helper(root, [])
        return result

    def helper(self, root, t):
        if root:
            for child in root.children:
                t.append(child.val)
                t = self.helper(child, t)
            return t
