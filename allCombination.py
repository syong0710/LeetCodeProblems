
def combine(n:int, k:int):
    res = []
    path = []
    def backtrack(n, k, StartIndex):
        print(path)
        if len(path) == k:
            res.append(path[:])
            print("output the results")
            return
        for i in range(StartIndex, n + 1):
            path.append(i)
            backtrack(n, k, i+1)
            path.pop()
            print("pop the path")
            print(path)
    backtrack(n, k, 1)
    return res


n = 4
k = 2
result = combine(n,k)
print(result)

