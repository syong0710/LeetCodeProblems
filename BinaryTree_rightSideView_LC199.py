class TreeNode:
    def __init__(self, nodeValue):
        self.value = nodeValue
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, rootValue):
        self.root = TreeNode(rootValue)

    def levelOrderTrav(self, root:TreeNode) ->list:
        if root is None:
            return []
        nodeQue = []
        nodeQue.append(root)
        nodeList = []
        while nodeQue:
            for _ in range(len(nodeQue)):
                nodeTmp = nodeQue.pop(0)
                nodeList.append(nodeTmp.value)
                if nodeTmp.left:
                    nodeQue.append(nodeTmp.left)
                if nodeTmp.right:
                    nodeQue.append(nodeTmp.right)
        return nodeList




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
               2    3
              / \ 
             4   5
            /\   
           8  9

"""
print("The level-order traversla of the tree: " + str(btree1.levelOrderTrav(btree1.root)))
#print("The right-side view of the binary tree: " + str(btree1.rightSideView(btree1.root)))