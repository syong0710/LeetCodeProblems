class TreeNode:
    def __init__(self, inputValue):
        self.value = inputValue
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, rootValue):
        self.root = TreeNode(rootValue)

    def inOrdertrav_recursive(self, root:TreeNode):
        # The local function for traversal
        def inOrderTrav(root:TreeNode):
            if root is None:
                return
            inOrderTrav(root.left)
            result.append(root.value)
            inOrderTrav(root.right)
        # The procedure
        result = []
        inOrderTrav(root)
        return result

    def preOrdertrav_recursive(self, root:TreeNode):
        # The local function for traversal
        def preOrderTrav(root:TreeNode):
            if root is None:
                return
            result.append(root.value)
            preOrderTrav(root.left)
            preOrderTrav(root.right)
        # The procedure
        result = []
        preOrderTrav(root)
        return result

    def preOrdertrav_recursive_lv(self, root:TreeNode):
        # The local function for traversal
        def preOrderTrav(root:TreeNode):
            if root is None:
                return
            levelTmp = level.pop(0)
            # Process the Node
            if levelTmp >= len(result):
                for _ in range(len(result), levelTmp+1):
                    result.append([])
            result[levelTmp].append(root.value)
            # The left child
            if root.left:
                level.append(levelTmp + 1)
                preOrderTrav(root.left)
            # The right child
            if root.right:
                level.append(levelTmp + 1)
                preOrderTrav(root.right)
        # The procedure
        level = []
        level.append(0)
        result = []
        preOrderTrav(root)
        return result

    def inOrdertrav_recursive_lv(self, root:TreeNode):
        # The local function for traversal
        def inOrderTrav(root:TreeNode):
            if root is None:
                return
            levelTmp = level.pop(0)
            # The left child
            if root.left:
                level.append(levelTmp + 1)
                inOrderTrav(root.left)
            # Process the Node
            if levelTmp >= len(result):
                for _ in range(len(result), levelTmp+1):
                    result.append([])
            result[levelTmp].append(root.value)
            # The right child
            if root.right:
                level.append(levelTmp + 1)
                inOrderTrav(root.right)
        # The procedure
        level = []
        level.append(0)
        result = []
        inOrderTrav(root)
        return result

    # Output all the path to the leaves
    def preOrdertrav_recursive_path(self, root:TreeNode):
        # The local function for traversal
        def preOrderTrav_path(root:TreeNode, path):
            if root is None:
                return
            # Process the Node
            path += str(root.value)
            if root.left is None and root.right is None:
                result.append(path)
                return
            # The left child
            if root.left:
                preOrderTrav_path(root.left, path+"->")
            # The right child
            if root.right:
                preOrderTrav_path(root.right, path+"->")
        # The procedure
        result = []
        path = ''
        preOrderTrav_path(root, path)
        return result


    # path Sum
    def pathSum(self, root:TreeNode):
        def allPath(root: TreeNode, path, sum_of_path):
            if root is None:
                return
            path += str(root.value)
            sum_of_path += root.value
            if root.left is None and root.right is None:
                result.append(path)
                result_sum.append(sum_of_path)
                return
            if root.left:
                allPath(root.left, path + "->", sum_of_path)
            if root.right:
                allPath(root.right, path + "->", sum_of_path)
        result_sum = []
        sum_of_path = 0
        result = []
        path = ''
        allPath(root, path, sum_of_path)
        return result, result_sum

    # The height of the tree (from the bottom go upward)
    def maxHeight(self, root:TreeNode) -> int:
        def postOrderTrav(root:TreeNode):
            if root is None:
                return 0
            heightLeft = postOrderTrav(root.left)
            heightRight = postOrderTrav(root.right)
            height = max(heightLeft,heightRight) + 1
            return height
        height = 0
        height = postOrderTrav(root)
        return height

    # The maximum depth of the tree (from the top go downward)
    def maxDepth(self, root:TreeNode)->int:
        def preOrderTrav(root:TreeNode, depth):
            result_depth.append(depth)
            # print("result depth=" + str(result_depth))
            if root.left is None and root.right is None:
                return
            if root.left:
                depth = depth + 1
                preOrderTrav(root.left, depth)
                depth = depth - 1
            if root.right:
                depth = depth + 1
                preOrderTrav(root.right, depth)
                depth = depth - 1
            return result_depth

        if root is None:
            return 0
        result_depth = []
        result_depth = preOrderTrav(root, 1)
        maxDepth = max(result_depth)
        return maxDepth


    # if the tree is balanced
    def isBalanced(self, root:TreeNode) -> bool:
        # get Height using the post-order traversal, go upward from the bottom
        # (get Depth using the pre-order traversal, go downward from the top)
        def getHeight(root:TreeNode) -> int:
            # The condition of return: terminate until meeting the None node
            if root is None:
                return 0
            left = getHeight(root.left)
            # print("left height = " + str(left) + "; root=" +str(root.value))
            if left == -1:
                return -1
            right = getHeight(root.right)
            # print("right height = " + str(right) + "; root=" +str(root.value))
            if right == -1:
                return -1
            if abs(left-right)>1:
                return -1
            else:
                return 1+max(left, right)
        # The procedure
        if getHeight(root) != -1:
            return True
        else:
            return False


##
###
##            1
#          /    \
#         2       3
#       /  \
#      4    5
#            \
#             7

binaryTree1 = BinaryTree(1)
binaryTree1.root.left = TreeNode(2)
binaryTree1.root.right = TreeNode(3)
binaryTree1.root.left.left = TreeNode(4)
binaryTree1.root.left.right = TreeNode(5)
binaryTree1.root.left.right.right = TreeNode(7)

print("In-order traversal with recursion of the tree: " + str(binaryTree1.inOrdertrav_recursive(binaryTree1.root)))
print("In-order traversal with recursion of the tree: " + str(binaryTree1.inOrdertrav_recursive_lv(binaryTree1.root)))
print("Pre-order traversal with recursion of the tree: " + str(binaryTree1.preOrdertrav_recursive(binaryTree1.root)))
print("Pre-order traversal with recursion of the tree: " + str(binaryTree1.preOrdertrav_recursive_lv(binaryTree1.root)))
print("All path (pre-order traversal, recursive): " + str(binaryTree1.preOrdertrav_recursive_path(binaryTree1.root)))


result_path, result_sum_path = binaryTree1.pathSum(binaryTree1.root)
print("All path of the tree: " + str(result_path))
print("All path sum: " + str(result_sum_path))

print(binaryTree1.isBalanced(binaryTree1.root))

print("The maximum height of the tree:" + str(binaryTree1.maxHeight(binaryTree1.root)))
print("The maximum depth of the tree:" + str(binaryTree1.maxDepth(binaryTree1.root)))


