class TreeNode:
    def __init__(self, nodeValue):
        self.value = nodeValue
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, rootValue):
        self.root = TreeNode(rootValue)

    def nodeMaxDepth(self, root:TreeNode)->int:
        return self.nodeDepth(root)[-1]

    def nodeDepthsSum(self, root:TreeNode)->int:
        return sum(self.nodeDepth(root))


    def nodeDepth(self, root:TreeNode) ->list:
        if root is None:
            return []
        nodeQue = []
        nodeQue.append(root)
        depthQue = []
        depthQue.append(0)
        depthList = []
        while nodeQue:
            for _ in range(len(nodeQue)):
                nodeTemp = nodeQue.pop(0)
                depthTemp = depthQue.pop(0)
                depthList.append(depthTemp)
                if nodeTemp.left:
                    nodeQue.append(nodeTemp.left)
                    depthQue.append(depthTemp+1)
                if nodeTemp.right:
                    nodeQue.append(nodeTemp.right)
                    depthQue.append(depthTemp + 1)
        return depthList


    # PreOrderTraversal get all depth
    def getDepthMax(self, root:TreeNode) -> int:
        if root is None:
            return 0
        depthList = []
        self.getDepth_preOrder(root, 1, depthList)
        return max(depthList)

    def getDepthMin(self, root:TreeNode) -> int:
        if root is None:
            return 0
        depthList = []
        self.getDepth_preOrder(root, 1, depthList)
        return min(depthList)

    def getDepth_preOrder(self, node:TreeNode, depthTemp:int, depthList:list):
        if node.left is None and node.right is None:
            depthList.append(depthTemp)
        depthTemp += 1
        if node.left:
            self.getDepth_preOrder(node.left, depthTemp, depthList)
        if node.right:
            self.getDepth_preOrder(node.right, depthTemp, depthList)



btree1 = BinaryTree(1)
btree1.root.left = TreeNode(2)
btree1.root.right = TreeNode(3)
btree1.root.left.left = TreeNode(4)
btree1.root.left.right = TreeNode(5)
btree1.root.left.left.left = TreeNode(8)
btree1.root.left.left.right = TreeNode(9)

"""
                  1
                /  \
               2     3
              / \ 
             4   5
            /\   
           8  9

"""

print("The level-order depth list: " + str(btree1.nodeDepth(btree1.root)))
print("The maximum depth: " + str(btree1.nodeMaxDepth(btree1.root)))
print("The node depths sum: " + str(btree1.nodeDepthsSum(btree1.root)))

print("The max depth (pre-order): " + str(btree1.getDepthMax(btree1.root)))
print("The min depth (pre-order): " + str(btree1.getDepthMin(btree1.root)))
