class TreeNode:
    def __init__(self, nodeValue:int):
        self.value = nodeValue
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, rootValue:int):
        self.root = TreeNode(rootValue)

    # in order traversal of the binayr tree
    def inOrderTrav(self, root:TreeNode) -> list:
        if root is None:
            return []
        nodeList = []
        self.inOrderRecur(root, nodeList)
        return nodeList

    # level-order traversal of the tree:
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

    # ALL PATH: pre-order traversal
    def allPath(self, root:TreeNode)->list:
        if root is None:
            return []
        path = []
        result = []
        self.preOrderAllPath(root, path, result)
        return result

    def preOrderAllPath(self, root: TreeNode, path: list, result:list):
        path.append(root.value)
        # When the node is leaf node we will update our result array
        if root.left is None and root.right is None:
            result.append(path.copy())
            #result.append(path[:])
            #print(path)
            del path[-1]
            return
        # recursively going left and right until we find the leaf and updating the array simultaneously
        if root.left:
            self.preOrderAllPath(root.left, path, result)
        if root.right:
            self.preOrderAllPath(root.right, path, result)
        del path[-1]

    def checkPathSum(self, root:TreeNode, targetSum:int)->list:
        pathSumList = []
        pathList = self.allPath(root)
        for i in range(len(pathList)):
            if sum(pathList[i])==targetSum:
                pathSumList.append(pathList[i].copy())
        return pathSumList


btree1 = BinaryTree(5)
btree1.root.left = TreeNode(4)
btree1.root.right = TreeNode(8)
btree1.root.left.left = TreeNode(11)
btree1.root.right.left = TreeNode(13)
btree1.root.right.right = TreeNode(4)
btree1.root.left.left.left = TreeNode(7)
btree1.root.left.left.right = TreeNode(2)
btree1.root.right.right.left = TreeNode(5)
btree1.root.right.right.right = TreeNode(1)
btree1.root.right.right.right = TreeNode(1)
btree1.root.right.right.right = TreeNode(1)
btree1.root.right.right.right.right = TreeNode(9)


"""
               5
          /           \
        4              8
       /              /   \
     11              13    4     
    /   \                 /  \  
   7     2               5     1
                                \
                                 9
"""

print("The level-order traversal of the binary tree: " + str(btree1.levelOrderTrav(btree1.root)))
print("All the paths to the leaves: " + str(btree1.allPath(btree1.root)))

#sum_of_path = 27
sum_of_path = 22
print("The paths with sum of path equal to " + str(sum_of_path) + " is " + str(btree1.checkPathSum(btree1.root, sum_of_path)))