class TreeNode:
    def __init__(self, nodeValue:int):
        self.value = nodeValue
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self, rootValue:int):
        self.root = TreeNode(rootValue)

    def numberOfNodes_levOrder(self, root:TreeNode) -> int:
        if root is None:
            return 0
        numOfNodes = 0
        nodeStack = []
        nodeStack.append(root)
        while nodeStack:
            for _ in range(len(nodeStack)):
                nodeTemp = nodeStack.pop(0)
                numOfNodes += 1
                if nodeTemp.left:
                    nodeStack.append(nodeTemp.left)
                if nodeTemp.right:
                    nodeStack.append(nodeTemp.right)
        return numOfNodes




binaryTree1 = BinaryTree(1)
binaryTree1.root.left = TreeNode(2)
binaryTree1.root.right = TreeNode(3)
binaryTree1.root.left.left = TreeNode(4)
binaryTree1.root.left.right = TreeNode(5)
binaryTree1.root.right.left = TreeNode(6)


print("The number of nodes of the binary tree: " + str(binaryTree1.numberOfNodes_levOrder(binaryTree1.root)))


