def binarySearch(nums:list, target:int) -> int:
    leftPointer = 0
    rightPointer = len(nums)-1

    # Check the element out of the array:
    if target < nums[leftPointer] or target > nums[rightPointer]:
        return -1

    while leftPointer <= rightPointer:
        midPointer = leftPointer + round(0.5 * (rightPointer - leftPointer))
        if target < nums[midPointer]:
            rightPointer = midPointer - 1
        elif target > nums[midPointer]:
            leftPointer = midPointer + 1
        elif target == nums[midPointer]:
            return midPointer
    return -1


array = [2, 5, 7, 9, 11, 24, 55, 99]
target = 11
print(binarySearch(array, target))
