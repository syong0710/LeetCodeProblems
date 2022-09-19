class TreeNode:
    def __init__(self, nodeValue:int):
        self.value = nodeValue
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, rootValue:int):
        self.root = TreeNode(rootValue)

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

    # The list of all leaves
    def allLeaves(self, root:TreeNode) -> list:
        if root is None:
            return []
        leaves_list = []
        self.preOrderLeaves(root, leaves_list)
        return leaves_list

    def preOrderLeaves(self, root:TreeNode, leavesList:list):
        if root is None:
            return
        if root.left and root.left.left is None and root.left.right is None:
            leavesList.append(root.left.value)
        if root.left:
            self.preOrderLeaves(root.left, leavesList)
        if root.right:
            self.preOrderLeaves(root.right, leavesList)
        return leavesList



btree1 = BinaryTree(5)
btree1.root.left = TreeNode(4)
btree1.root.right = TreeNode(8)
btree1.root.left.left = TreeNode(11)
btree1.root.right.left = TreeNode(13)
btree1.root.right.right = TreeNode(4)
btree1.root.left.left.left = TreeNode(7)
btree1.root.left.left.right = TreeNode(2)
btree1.root.left.left.right.left = TreeNode(12)
btree1.root.left.left.right.right = TreeNode(13)
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
        /  \                      \
       12   13                      9
"""

print("Pre-order traversal of the binary tree: " + str(btree1.levelOrderTrav(btree1.root)))
print("The heaves of the binary tree: " + str(btree1.allLeaves(btree1.root)))
