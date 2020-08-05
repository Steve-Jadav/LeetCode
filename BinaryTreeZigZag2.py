# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return root

        traversal = list()
        queue = deque()
        queue.append(root)
        flag = True

        while queue:
            nextLevel = deque()
            qLen = len(queue)

            for i in range(0, qLen):
                node = queue.popleft()

                if flag:
                    nextLevel.append(node.val)
                else:
                    nextLevel.appendleft(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            traversal.append(nextLevel)
            flag = not flag

        return traversal
        
