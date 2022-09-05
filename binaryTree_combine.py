class TreeNode:
    def __init__(self, nodeValue:int):
        self.value = nodeValue
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self,rootValue:int):
        self.root = TreeNode(rootValue)

    def inOrderTrav_list(self, root:TreeNode):
        result = []
        if root is None:
            return []
        self.inOrderTrav(root, result)
        return result

    def inOrderTrav(self, root:TreeNode, result):
        if root is None:
            return
        self.inOrderTrav(root.left, result)
        result.append(root.value)
        self.inOrderTrav(root.right, result)

    def levelOrderTrav(self, root:TreeNode):
        if root is None:
            return []
        result = []
        nodeQue = []
        nodeQue.append(root)
        while nodeQue:
            for _ in nodeQue:
                nodeTemp = nodeQue.pop(0)
                result.append(nodeTemp.value)
                if nodeTemp.left:
                    nodeQue.append(nodeTemp.left)
                if nodeTemp.right:
                    nodeQue.append(nodeTemp.right)
        return result

    # merge tree2 into tree1 using interative method
    def mergeTwoTrees_iterative(self, root1:TreeNode, root2:TreeNode):
        if root1 is None and root2:
            return root2
        if root1 and root2 is None:
            return root1

        nodeQue = []
        nodeQue.append(root1)
        nodeQue.append(root2)

        while nodeQue:
            for _ in nodeQue:
                nodeTemp1 = nodeQue.pop(0)
                nodeTemp2 = nodeQue.pop(0)
                nodeTemp1.value = nodeTemp1.value + nodeTemp2.value

                if nodeTemp1.left and nodeTemp2.left:
                    nodeQue.append(nodeTemp1.left)
                    nodeQue.append(nodeTemp2.left)
                if nodeTemp1.right and nodeTemp2.right:
                    nodeQue.append(nodeTemp1.right)
                    nodeQue.append(nodeTemp2.right)

                if nodeTemp1.left is None and nodeTemp2.left:
                    nodeTemp1.left = nodeTemp2.left
                if nodeTemp1.right is None and nodeTemp2.right:
                    nodeTemp1.right = nodeTemp2.right
        return root1

    # merge tree2 into tree1 using recursive method
    def mergeTwoTrees_recursive(self, root1: TreeNode, root2: TreeNode):
        if root1 is None and root2:
            return root2
        if root1 and root2 is None:
            return root1

        root1.value = root1.value + root2.value
        root1.left = self.mergeTwoTrees_recursive(root1.left, root2.left)
        root1.right = self.mergeTwoTrees_recursive(root1.right, root2.right)
        return root1

"""
           1
        /     \
      2         3
    /   \
   4     5
   
"""
btree1 = BinaryTree(1)
btree1.root.left = TreeNode(2)
btree1.root.right = TreeNode(3)
btree1.root.left.left = TreeNode(4)
btree1.root.left.right = TreeNode(5)

"""
           11
        /     \
      12        13
               /  \
             14   15

"""
btree2 = BinaryTree(11)
btree2.root.left = TreeNode(12)
btree2.root.right = TreeNode(13)
btree2.root.right.left = TreeNode(14)
btree2.root.right.right = TreeNode(15)


#print("in-order traversal of the binary tree1: " + str(btree1.inOrderTrav_list(btree1.root)))
print("level-order traversal of the binary tree1: " + str(btree1.levelOrderTrav(btree1.root)))

#print("in-order traversal of the binary tree2: " + str(btree2.inOrderTrav_list(btree2.root)))
print("level-order traversal of the binary tree2: " + str(btree2.levelOrderTrav(btree2.root)))

#btree1.root = btree1.mergeTwoTrees_iterative(btree1.root, btree2.root)
btree1.root = btree1.mergeTwoTrees_recursive(btree1.root, btree2.root)
print("level-order traversal of the binary tree1: " + str(btree1.levelOrderTrav(btree1.root)))

