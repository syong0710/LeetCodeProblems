class TreeNode:
    def __init__(self, nodeValue):
        self.value = nodeValue
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self, rootValue):
        self.root = TreeNode(rootValue)


    def lvOrderTrav(self, root:TreeNode)->list:
        if root is None:
            return []
        nodeQue = []
        nodeQue.append(root)
        valueList = []
        while nodeQue:
            for _ in range(len(nodeQue)):
                nodeTemp = nodeQue.pop(0)
                valueList.append(nodeTemp.value)
                if nodeTemp.left:
                    nodeQue.append(nodeTemp.left)
                if nodeTemp.right:
                    nodeQue.append(nodeTemp.right)
        return valueList

    def invertTree(self, root:TreeNode):
        if root is None:
            return
        nodeQue = []
        nodeQue.append(root)
        while nodeQue:
            for _ in range(len(nodeQue)):
                nodeTemp = nodeQue.pop(0)
                nodeTemp.left, nodeTemp.right = nodeTemp.right, nodeTemp.left
                if nodeTemp.left:
                    nodeQue.append(nodeTemp.left)
                if nodeTemp.right:
                    nodeQue.append(nodeTemp.right)


btree1 = BinaryTree(4)
btree1.root.left = TreeNode(2)
btree1.root.right = TreeNode(7)
btree1.root.left.left = TreeNode(1)
btree1.root.left.right = TreeNode(3)
btree1.root.right.left = TreeNode(6)


"""
            4
          /   \
        2       7
      /   \    /  
    1     3   6    


"""
print(btree1.lvOrderTrav(btree1.root))

btree1.invertTree(btree1.root)
print("the inverted/mirrored tree: " + str(btree1.lvOrderTrav(btree1.root)))

