## solve two-sum using harsh table
def twoSum(array, target):
    twoSumMap = dict()
    for i in range(0, len(array)):
        harshKey = target - array[i]
        if array[i] in twoSumMap:
            return [i, twoSumMap.get(array[i])]
        else:
            twoSumMap[harshKey] = i
    return []


array = [1, 5, 2, 8, 3]
target = 10

print(str(twoSum(array, target)))

