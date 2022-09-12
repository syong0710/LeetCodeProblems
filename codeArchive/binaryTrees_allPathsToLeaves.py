class TreeNode:
    def __init__(self, nodeValue):
        self.value = nodeValue
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, rootValue):
        self.root = TreeNode(rootValue)

    # The in-order traversal, with iterative stack
    def inOrderTrav_iterative(self, root:TreeNode)->list:
        if root is None:
            return []
        record = []
        stack = []
        stack.append(root)
        while stack:
            nodeTemp = stack.pop()
            if nodeTemp is not None:
                # in-order traversal
                # stack the right child first, then the node, at last the left child
                if nodeTemp.right:
                    stack.append(nodeTemp.right)
                stack.append(nodeTemp)
                # The current node is marked using None
                stack.append(None)
                if nodeTemp.left:
                    stack.append(nodeTemp.left)
            else:
                # Only the None-marked element in the stack will be recorded
                nodeTemp = stack.pop()
                record.append(nodeTemp.value)
        return record

    # The in-order traversal, with iterative stack. The level will be output
    def inOrderTrav_iterative_lv(self, root:TreeNode)->list:
        if root is None:
            return []
        record = []
        stackLv = [] #The stack storing the level information
        stackLv.append(0)
        stack = []
        stack.append(root)
        while stack:
            nodeTemp = stack.pop()
            nodeLv = stackLv.pop()
            if nodeTemp is not None:
                # in-order traversal
                # stack the right child first, then the node, at last the left child
                if nodeTemp.right:
                    stack.append(nodeTemp.right)
                    stackLv.append(nodeLv+1)
                stack.append(nodeTemp)
                stackLv.append(nodeLv)
                # The current node is marked using None
                stack.append(None)
                stackLv.append(None)
                if nodeTemp.left:
                    stack.append(nodeTemp.left)
                    stackLv.append(nodeLv+1)
            else:
                # Only the None-marked element in the stack will be recorded
                nodeTemp = stack.pop()
                nodeLv = stackLv.pop()
                if nodeLv>=len(record):
                    for _ in range(0, nodeLv+1):
                        record.append([])
                record[nodeLv].append(nodeTemp.value)
        return record

    # All the path from the root to the leaves
    def inOrderTrav_iterative_allPath(self, root:TreeNode)->list:
        if root is None:
            return []
        #record = []
        record_path = []
        stack = []
        stack.append(root)
        pathStack = [] # The stack for path storage
        pathStack.append(str(root.value))
        while stack:
            nodeTemp = stack.pop()
            pathTemp = pathStack.pop()
            if nodeTemp is not None:
                # stack the right child
                if nodeTemp.right:
                    stack.append(nodeTemp.right)
                    pathStack.append(pathTemp + "->" + str(nodeTemp.right.value))
                # stack the node
                stack.append(nodeTemp)
                stack.append(None) # The current node is marked using None
                # avoid double-counting the leves
                if nodeTemp.right or nodeTemp.left:
                    pathStack.append(pathTemp + "->" + str(nodeTemp.value))
                else:
                    pathStack.append(pathTemp)
                # stack the left child
                if nodeTemp.left:
                    stack.append(nodeTemp.left)
                    pathStack.append(pathTemp + "->" + str(nodeTemp.left.value))
            else:
                # Only the None-marked element in the stack will be recorded
                nodeTemp = stack.pop()
                #record.append(nodeTemp.value)
                if nodeTemp.left is None and nodeTemp.right is None:
                    record_path.append(pathTemp) #output the path only when a leaf is detected
        return record_path


    # PreOrder would be much easier, without the double-counted leaf issue
    # since the node visted is exactely the node to be processed
    def postOrderTrav_iterative_allPath_simplified(self, root:TreeNode):
        if root is None:
            return []
        stack = []
        stack.append(root)
        pathStack = []
        pathStack.append(str(root.value))
        record = []
        recordPath = []
        while stack:
            nodeTmp = stack.pop()
            record.append(nodeTmp.value)
            pathTmp = pathStack.pop()
            # if the leaf is detected, output the path
            if nodeTmp.right is None and nodeTmp.left is None:
                recordPath.append(pathTmp)
            if nodeTmp.right:
                stack.append(nodeTmp.right)
                pathStack.append(pathTmp + "->" + str(nodeTmp.right.value))
            if nodeTmp.left:
                stack.append(nodeTmp.left)
                pathStack.append(pathTmp + "->" + str(nodeTmp.left.value))
        return recordPath, record

#
#            1
#          /   \
#         2     3
#       /  \    /
#      4    5  6
#

btree1 = BinaryTree(1)
btree1.root.left = TreeNode(2)
btree1.root.right = TreeNode(3)
btree1.root.left.left = TreeNode(4)
btree1.root.left.right = TreeNode(5)
btree1.root.right.left = TreeNode(6)

print("In-order iterative traversal: " + str(btree1.inOrderTrav_iterative(btree1.root)))
print("In-order iterative traversal with level: " + str(btree1.inOrderTrav_iterative_lv(btree1.root)))
print("In-order all path:" + str(btree1.inOrderTrav_iterative_allPath(btree1.root)))

postOrderPath, postOrderRecord = btree1.postOrderTrav_iterative_allPath_simplified(btree1.root)
print("Post-order iterative traversal" + str(postOrderRecord))
print("Post-order all path:" + str(postOrderPath))

