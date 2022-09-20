#"""
def squaresSortedArray(nums:list[int]) -> list:
    if nums is None or len(nums)==0:
        return nums
    listLen = len(nums)
    left = 0
    right = listLen -1
    result = [None] * listLen
    while left <= right:
        for i in range(listLen):
            leftSqr = nums[left] ** 2
            rightSqr = nums[right] ** 2
            if leftSqr <= rightSqr:
                result[listLen-1-i] = rightSqr
                right -= 1
            elif leftSqr > rightSqr:
                result[listLen-1-i] = leftSqr
                left += 1
            #print(result)
    return result
#"""

nums = [-7, -3, 2, 3, 11]
print("The squares of a sorted array: " + str(squaresSortedArray(nums)))
