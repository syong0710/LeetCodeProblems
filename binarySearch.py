def binarySearch(inputArray, searchNum: int) -> int:
    leftPointer: int = 0;
    rightPointer: int = len(inputArray) - 1

    # pop put for the extreme cases
    if searchNum < inputArray[leftPointer] or searchNum > inputArray[rightPointer]:
        return -1

    while leftPointer <= rightPointer:
        midPointer = leftPointer + round((rightPointer - leftPointer) / 2)
        if searchNum < inputArray[midPointer]:
            rightPointer = midPointer - 1
        if searchNum > inputArray[midPointer]:
            leftPointer = midPointer + 1
        if searchNum == inputArray[midPointer]:
            return midPointer
    return -1


nums = [2, 3, 5, 13, 24, 90]
searchNum = 13
print("The index of the key number: " + str(binarySearch(nums, searchNum)))
