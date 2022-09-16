class TreeNode:
    def __init__(self, nodeValue:int):
        self.value = nodeValue
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, rootValue:int):
        self.root = TreeNode(rootValue)

    def levelOrderTrav(self, root:TreeNode) -> list:
        if root is None:
            return []
        nodeQue = []
        nodeQue.append(root)
        result = []
        while nodeQue:
            for _ in range(len(nodeQue)):
                nodeTemp = nodeQue.pop(0)
                result.append(nodeTemp.value)
                if nodeTemp.left:
                    nodeQue.append(nodeTemp.left)
                if nodeTemp.right:
                    nodeQue.append(nodeTemp.right)
        return result

    def mergeTrees(self, root1:TreeNode, root2:TreeNode) -> TreeNode:
        if root1 is None:
            return root2
        if root2 is None:
            return root1

        nodeQue = []
        nodeQue.append(root1)
        nodeQue.append(root2)
        while nodeQue:
            nodeTmp1 = nodeQue.pop(0)
            nodeTmp2 = nodeQue.pop(0)

            # update the Que
            if nodeTmp1.left and nodeTmp2.left:
                nodeQue.append(nodeTmp1.left)
                nodeQue.append(nodeTmp2.left)
            if nodeTmp1.right and nodeTmp2.right:
                nodeQue.append(nodeTmp1.right)
                nodeQue.append(nodeTmp2.right)

            # proceed the node
            nodeTmp1.value += nodeTmp2.value
            if nodeTmp1.left is None and nodeTmp2.left:
                nodeTmp1.left = nodeTmp2.left
            if nodeTmp1.right is None and nodeTmp2.right:
                nodeTmp1.right = nodeTmp2. right
        return root1


btree1 = BinaryTree(1)
btree1.root.left = TreeNode(2)
btree1.root.right = TreeNode(3)
btree1.root.left.left = TreeNode(4)
btree1.root.left.right = TreeNode(5)

btree2 = BinaryTree(11)
btree2.root.left = TreeNode(12)
btree2.root.right = TreeNode(13)
btree2.root.right.left = TreeNode(14)
btree2.root.right.right = TreeNode(15)
btree2.root.right.right.left = TreeNode(16)
btree2.root.right.right.right = TreeNode(17)

"""
TREE1:
                      1
                  /        \
                 2          3
               /   \  
             4       5

TREE2:
                      11
                  /        \
                12          13
                           /   \  
                         14      15
                                /   \
                               16    17 


"""
print("level order traversal of tree1: " + str(btree1.levelOrderTrav(btree1.root)))
print("level order traversal of tree2: " + str(btree2.levelOrderTrav(btree2.root)))

tree_1_2 = btree1.mergeTrees(btree1.root, btree2.root)
print("level order traversal of the merged tree1 and tree2: " + str(btree1.levelOrderTrav(tree_1_2)))












