def binarySearch(inputArray, searchNum:int) ->int:
    leftPointer:int = 0;
    rightPointer:int = len(inputArray) -1
    midPointer:int = leftPointer + round((rightPointer-leftPointer)/2)

    # pop put for the extreme cases
    if searchNum<inputArray[leftPointer] or searchNum>inputArray[rightPointer]:
        return []

    while leftPointer <= rightPointer:
        midPointer = leftPointer + round((rightPointer - leftPointer) / 2)
        if searchNum < inputArray[midPointer]:
            rightPointer = midPointer
        if searchNum > inputArray[midPointer]:
            leftPointer = midPointer+1
        if searchNum == inputArray[midPointer]:
            return midPointer
    return []

nums = [2, 3, 5, 13, 24, 90]
searchNum = 90
print("The index of the key number: "+str(binarySearch(nums,searchNum)))
    
