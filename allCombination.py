class Solution1:
    # list all the combination of the array range(1 n+1), with k elements
    def combine(n:int, k:int):
        res = []
        path = []
        def backtrack(n, k, startIndex):
            # Check the condition of return
            if len(path) == k:
                res.append(path[:])
                return
            # The width of search is determined by the for loop
            for i in range(startIndex, n + 1):
                path.append(i) # take one step forward
                backtrack(n, k, i+1) # the depth of search is determined by the recursive function
                path.pop() # take one step back
        backtrack(n, k, 1)
        return res

class Solution2:
    def combine_improve(n:int, k:int):
        res = []
        path = []
        def backtrack_improve(n, k, startIndex):
            if len(path) == k:
                res.append(path[:])
                return
            #已经选择的元素个数：path.size();
            #还需要的元素个数为: k - path.size();
            #在集合n中至多要从该起始位置: n - (k - path.size()) + 1，开始遍历
            for i in range(startIndex, n-(k-len(path))+2):
                path.append(i)
                backtrack_improve(n, k, i + 1)
                path.pop()
        backtrack_improve(n, k, 1)
        return res


n = 4
k = 2
result1 = Solution1.combine(n,k)
print(result1)

result2 = Solution2.combine_improve(n,k)
print(result2)



#
##################################################################
# ******** The illustration of combine(n:int, k:int)  ***********
##################################################################
#
#  backtrack(4,2,1) -> startIndex=1, i=1 -> path=[1] -> backtrack(4,2,2)                                                 path = []
#                                                       \                                                                       /
#                                                    startIndex=2, i=2 -> path=[1,2] -> backtrack(4,2,3)    path=[1]           /
#                                                                                                   \        /                /
#                                                                                                   res=[[1,2]]              /
#                                                                                                                           /
#                                                    startIndex=2, i=3 -> path=[1,3] -> backtrack(4,2,4)   path=[1]        /
#                                                                                                   \       /             /
#                                                                                              res=[[1,2], [1,3]]        /
#                                                                                                                       /
#                                                    startIndex=2, i=4 -> path=[1,4] -> backtrack(4,2,5)     path=[1]  /
#                                                                                                    \       /        /
#                                                                                          res=[[1,2], [1,3], [1,4]] --
#                     startIndex=1, i=2 -> path=[2] -> backtrack(4,2,3)                                           path = []
#                                                            \                                                            /
#                                                    startIndex=3, i=3 -> path=[2,3] -> backtrack(4,2,4)    path=[2]     /
#                                                                                                   \        /          /
#                                                                                 res=[[1,2], [1,3], [1,4], [2,3]]     /
#                                                    startIndex=3, i=4 -> path=[2,4] -> backtrack(4,2,5)    path=[2]  /
#                                                                                                   \        /       /
#                                                                             res=[[1,2], [1,3], [1,4], [2,3], [2,4]]
#                     startIndex=1, i=3 -> path=[3] -> backtrack(4,2,4)                                               path = []
#                                                            \                                                              /
#                                                       startIndex=4, i=4 -> path=[2,4] -> backtrack(4,2,5)    path=[3]    /
#                                                                                                       \        /        /
#                                                                           res=[[1,2], [1,3], [1,4], [2,3], [2,4], [3,4]]
#                     startIndex=1, i=4 -> path=[4] -> backtrack(4,2,5)                          path = []
#                                                            \                                   /
#                                                       startIndex=5, i=5 for loop ends doing nothing
#
#
#
#
#
