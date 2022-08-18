# Operations based on level-order traversal of a binary tree #
# S.Yong (Aug 18, 2022)

# Level-order traversal of a binary-tree
# mirror the binary-tree
# if the tree is symmetrical
# The maximum depth of the tree
# The minimum depth of the tree
# The number of nodes
# The left-side view of the tree
# The right-side view of the tree


# The def of a binary tree node
class TreeNode:
    def __init__(self, nodeValue):
        self.value = nodeValue
        self.left = None
        self.right = None

class BinaryTree:
    # create a binary tree with the defined root
    def __init__(self, nodeValue):
        self.root = TreeNode(nodeValue)

    # level order traversal of the binary tree
    def levelOrderTrav_lv(self, root:TreeNode) -> list:
        if root is None:
            return []
        nodeQue = []
        nodeQue.append(root)
        lvQue = []
        lvQue.append(0)
        recQue = []
        while nodeQue:
            for _ in range(len(nodeQue)):
                nodeTmp = nodeQue.pop(0)
                lvTmp = lvQue.pop(0)
                if lvTmp>=len(recQue):
                    recQue.append([])
                recQue[lvTmp].append(nodeTmp.value)
                if nodeTmp.left:
                    nodeQue.append(nodeTmp.left)
                    lvQue.append(lvTmp+1)
                if nodeTmp.right:
                    nodeQue.append(nodeTmp.right)
                    lvQue.append(lvTmp+1)
        return recQue

    def mirrorTree(self, root:TreeNode):
        if root is None:
            return root
        nodeQue = []
        nodeQue.append(root)
        while nodeQue:
            for _ in range(len(nodeQue)):
                nodeTmp = nodeQue.pop(0)
                nodeTmp.left,nodeTmp.right = nodeTmp.right,nodeTmp.left
                if nodeTmp.left:
                    nodeQue.append(nodeTmp.left)
                if nodeTmp.right:
                    nodeQue.append(nodeTmp.right)


    # check if the tree is symmetrical using level-order transversal
    def isSymTree(self, root:TreeNode) -> bool:
        if root is None:
            #print("The root is void. False")
            return False
        nodeQue = []
        nodeQue.append(root.left)
        nodeQue.append(root.right)
        while nodeQue:
            leftTmp = nodeQue.pop(0)
            rightTmp = nodeQue.pop(0)
            # if both nodes are void, is symmtrical
            if leftTmp is None and rightTmp is None:
                #print("Both nodes are none. Contibue")
                continue
            # if only one node is void, or two nodes are not equal, return false
            elif leftTmp is None and rightTmp is not None:
                #print("Only one node is None. False")
                return False
            elif rightTmp is None and leftTmp is not None:
                #print("Only one node is None. False")
                return False
            elif rightTmp.value != leftTmp.value:
                #print("Two nodes are not equal. False")
                return False
            else:
                nodeQue.append(leftTmp.left)
                nodeQue.append(rightTmp.right)
                nodeQue.append(leftTmp.right)
                nodeQue.append(rightTmp.left)
                #print("two nodes are equal")
        return True

    # Return the maximum depth of a binary-tree
    def maxDepth(self, root:TreeNode) ->int:
        if root is None:
            return 0
        nodeQue = []
        nodeQue.append(root)
        nodeValQue = []
        nodeLvQue = []
        nodeLvQue.append(1)
        while nodeQue:
            nodeTmp = nodeQue.pop(0)
            nodeLvTmp = nodeLvQue.pop(0)
            nodeValQue.append(nodeTmp.value)
            #print(nodeTmp.value)
            #print(nodeLvTmp)
            if nodeTmp.left:
                nodeQue.append(nodeTmp.left)
                nodeLvQue.append(nodeLvTmp+1)
            if nodeTmp.right:
                nodeQue.append(nodeTmp.right)
                nodeLvQue.append(nodeLvTmp+1)
        return nodeLvTmp


    # Return the minumum depth of binary-tree
    def minDepth(self, root:TreeNode) -> int:
        if root is None:
            return 0
        nodeQue = []
        nodeQue.append(root)
        nodeValQue = []
        nodeLvQue = []
        nodeLvQue.append(1)
        while nodeQue:
            nodeTmp = nodeQue.pop(0)
            nodeLvTmp = nodeLvQue.pop(0)
            nodeValQue.append(nodeTmp.value)
            #print(nodeTmp.value)
            #print(nodeLvTmp)
            if nodeTmp.left:
                nodeQue.append(nodeTmp.left)
                nodeLvQue.append(nodeLvTmp+1)
            if nodeTmp.right:
                nodeQue.append(nodeTmp.right)
                nodeLvQue.append(nodeLvTmp+1)
            if nodeTmp.right is None and nodeTmp.right is None:
                #print("min leaf is found @ " + str(nodeTmp.value) )
                return nodeLvTmp
        return nodeLvTmp

    # return the number of nodes
    def numberOfNodes(self, root:TreeNode) -> int:
        if root is None:
            return 0
        nodeQue = []
        nodeQue.append(root)
        nodeValQue = []
        nodeNumTmp = 1
        while nodeQue:
            nodeTmp = nodeQue.pop(0)
            nodeValQue.append(nodeTmp.value)
            #print(nodeTmp.value)
            #print(nodeNumTmp)
            if nodeTmp.left:
                nodeQue.append(nodeTmp.left)
                nodeNumTmp = nodeNumTmp + 1
            if nodeTmp.right:
                nodeQue.append(nodeTmp.right)
                nodeNumTmp += 1
        return nodeNumTmp

    # The left-side view of the tree
    def leftSideView(self, root:TreeNode) -> list:
        if root is None:
            return []
        nodeQue = []
        nodeQue.append(root)
        lvQue = []
        lvQue.append(0)
        valueQue = []
        while nodeQue:
            for _ in range(len(nodeQue)):
                nodeTmp = nodeQue.pop(0)
                lvTmp = lvQue.pop(0)
                if lvTmp>=len(valueQue):
                    valueQue.append([])
                    valueQue[lvTmp].append(nodeTmp.value)
                if nodeTmp.left:
                    nodeQue.append(nodeTmp.left)
                    lvQue.append(lvTmp+1)
                if nodeTmp.right:
                    nodeQue.append(nodeTmp.right)
                    lvQue.append(lvTmp+1)
        return valueQue




    # The right-side view fo the tree
    def rightSideView(self, root:TreeNode) -> list:
        if root is None:
            return []
        nodeQue = []
        nodeQue.append(root)
        lvQue = []
        lvQue.append(0)
        valueQue = []
        while nodeQue:
            for _ in range(len(nodeQue)):
                nodeTmp = nodeQue.pop(0)
                lvTmp = lvQue.pop(0)
                if lvTmp>=len(valueQue):
                    valueQue.append([])
                    valueQue[lvTmp].append(nodeTmp.value)
                if nodeTmp.right:
                    nodeQue.append(nodeTmp.right)
                    lvQue.append(lvTmp+1)
                if nodeTmp.left:
                    nodeQue.append(nodeTmp.left)
                    lvQue.append(lvTmp+1)
        return valueQue





btree1 = BinaryTree(1)
btree1.root.left = TreeNode(2)
btree1.root.right = TreeNode(2)
btree1.root.left.left = TreeNode(3)
btree1.root.left.right = TreeNode(4)
btree1.root.right.left = TreeNode(4)
btree1.root.right.right = TreeNode(3)
#
#            1
#        /       \
#        2        2
#       / \     /   \
#      3   4   4     3


btree2 = BinaryTree(1)
btree2.root.left = TreeNode(2)
btree2.root.right = TreeNode(3)
#btree2.root.left.left = TreeNode(4)
#btree2.root.left.right = TreeNode(5)
btree2.root.right.left = TreeNode(6)
btree2.root.right.right = TreeNode(7)
#
#            1
#         /      \
#        2        3
#                /  \
#               6   7


print(btree1.levelOrderTrav_lv(btree1.root))
print("the number of nodes: " + str(btree1.numberOfNodes(btree1.root)))
print("if the tree is symmetrical: " + str(btree1.isSymTree(btree1.root)) )

print(btree2.levelOrderTrav_lv(btree2.root))
print("the left-side view of the tree" + str(btree2.leftSideView(btree2.root)))
print("the right-side view of the tree" + str(btree2.rightSideView(btree2.root)))
print("if the tree is symmetrical: " + str(btree2.isSymTree(btree2.root)) )
print("the maximum depth of the tree is: " + str(btree2.maxDepth(btree2.root)))
print("the minimum depth of the tree is: " + str(btree2.minDepth(btree2.root)))
print("the number of nodes: " + str(btree2.numberOfNodes(btree2.root)))
print("Mirror the tree:")
btree2.mirrorTree(btree2.root)
print(btree2.levelOrderTrav_lv(btree2.root))



