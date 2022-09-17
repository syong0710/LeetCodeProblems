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


    def leftSideView(self, root:TreeNode) -> list:
        if root is None:
            return []
        nodeQue = []
        nodeQue.append(root)
        levelQue = []
        levelQue.append(1)
        result = []
        result.append(root.value)
        level_max = 1

        while nodeQue:
            for _ in range(len(nodeQue)):
                nodeTemp = nodeQue.pop(0)
                levelTemp = levelQue.pop(0)

                if levelTemp > level_max:
                    level_max = levelTemp
                    result.append(nodeTemp.value)

                # search left first, then search right
                if nodeTemp.left:
                    nodeQue.append(nodeTemp.left)
                    levelQue.append(levelTemp+1)
                if nodeTemp.right:
                    nodeQue.append(nodeTemp.right)
                    levelQue.append(levelTemp+1)
        return result


    def rightSideView(self, root:TreeNode) -> list:
        if root is None:
            return []
        nodeQue = []
        nodeQue.append(root)
        levelQue = []
        levelQue.append(1)
        result = []
        result.append(root.value)
        level_max = 1

        while nodeQue:
            for _ in range(len(nodeQue)):
                nodeTemp = nodeQue.pop(0)
                levelTemp = levelQue.pop(0)

                if levelTemp > level_max:
                    level_max = levelTemp
                    result.append(nodeTemp.value)

                # search right first, then search left
                if nodeTemp.right:
                    nodeQue.append(nodeTemp.right)
                    levelQue.append(levelTemp+1)
                if nodeTemp.left:
                    nodeQue.append(nodeTemp.left)
                    levelQue.append(levelTemp+1)
        return result

    # The right-side view of the tree #2
    def rightSideView_2(self, root:TreeNode) -> list[int]:
        if root is None:
            return []
        nodeQue = []
        nodeQue.append(root)
        result = []
        while nodeQue:
            node_result = nodeQue[-1]
            result.append(node_result.value)
            for _ in range(len(nodeQue)):
                nodeTemp = nodeQue.pop(0)
                if nodeTemp.left:
                    nodeQue.append(nodeTemp.left)
                if nodeTemp.right:
                    nodeQue.append(nodeTemp.right)
        return result

    # The left-side view of the tree #2
    def leftSideView_2(self, root:TreeNode) -> list[int]:
        if root is None:
            return []
        nodeQue = []
        nodeQue.append(root)
        result = []
        while nodeQue:
            node_result = nodeQue[0]
            result.append(node_result.value)
            for _ in range(len(nodeQue)):
                nodeTemp = nodeQue.pop(0)
                if nodeTemp.left:
                    nodeQue.append(nodeTemp.left)
                if nodeTemp.right:
                    nodeQue.append(nodeTemp.right)
        return result


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
print("The left-side view of the binary tree: " + str(btree1.leftSideView(btree1.root)))
print("The right-side view of the binary tree: " + str(btree1.rightSideView(btree1.root)))



print("The left-side view of (#2) the binary tree: " + str(btree1.leftSideView_2(btree1.root)))
print("The right-side view of (#2) the binary tree: " + str(btree1.rightSideView_2(btree1.root)))
