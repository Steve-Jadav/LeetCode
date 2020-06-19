class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root: TreeNode = None
        self.head: TreeNode = None
        self.previous: TreeNode = None

    def BinaryTree2DoublyLinkedList(self, root: TreeNode):
        if root == None:
            return

        self.BinaryTree2DoublyLinkedList(root.left)

        if (self.previous == None):
            self.head = root
        else:
            root.left = self.previous
            self.previous.right = root
        self.previous = root

        self.BinaryTree2DoublyLinkedList(root.right)

    def printDLL(self, root: TreeNode):
        temp: TreeNode = root
        while temp:
            print (temp.val)
            temp = temp.right


if __name__ == "__main__":
    binaryTree = BinaryTree()
    binaryTree.root = TreeNode(10)
    binaryTree.root.left = TreeNode(12)
    binaryTree.root.right = TreeNode(15)
    binaryTree.root.left.left = TreeNode(25)
    binaryTree.root.left.right = TreeNode(30)
    binaryTree.root.right.left = TreeNode(36)

    # Convert the BT to a DLL
    binaryTree.BinaryTree2DoublyLinkedList(binaryTree.root)

    # Print DLL
    binaryTree.printDLL(binaryTree.head)
