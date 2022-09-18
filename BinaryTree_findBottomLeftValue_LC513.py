class TreeNode:
    def __init__(self, nodeValue):
        self.value = nodeValue
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, rootValue):
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

    def findBottomLeftValue(self, root:TreeNode) -> int:
        if root is None:
            return None
        nodeQue = []
        nodeQue.append(root)
        resultList = []
        while nodeQue:
            nodeLeft = nodeQue[0]
            resultList.append(nodeLeft.value)
            for _ in range(len(nodeQue)):
                nodeTemp = nodeQue.pop(0)
                if nodeTemp.left:
                    nodeQue.append(nodeTemp.left)
                if nodeTemp.right:
                    nodeQue.append(nodeTemp.right)
        return resultList[-1]


btree1 = BinaryTree(1)
btree1.root.left = TreeNode(2)
btree1.root.right = TreeNode(3)
btree1.root.left.left = TreeNode(4)
btree1.root.left.right = TreeNode(5)
#btree1.root.left.left.left = TreeNode(8)
btree1.root.left.left.right = TreeNode(9)

"""
                  1
                /  \
               2    3
              / \ 
             4   5
            /\   
           8  9

"""

print("The level-order traversal of the tree: " + str(btree1.levelOrderTrav(btree1.root)))
print("The bottom left node's value the tree: " + str(btree1.findBottomLeftValue(btree1.root)))





