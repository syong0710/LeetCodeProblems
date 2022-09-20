def twoSum(nums:int, target:int) -> list:
    if nums is None or len(nums)==0:
        return []
    # create a python dictionary and use it as hash tabel
    hashTable = dict()
    result = []
    for i in range(len(nums)):
        if nums[i] in hashTable:
            result.append(i)
            result.append(hashTable[nums[i]])
        else:
            key = target - nums[i]
            hashTable[key] = i
    return result

nums = [3, 1, 2, 7, 11, 15]
twoSumTarget = 9

print(str(twoSum(nums,twoSumTarget)))