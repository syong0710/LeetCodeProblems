def reverseString(inputArray:list) -> list:
    left = 0
    right = len(inputArray)-1
    while left<right:
        inputArray[left], inputArray[right] = inputArray[right], inputArray[left]
        left += 1
        right -= 1
    return inputArray


#array1 = ["a", "c", "d", "m", "n", "y", "z"]
array1 = ["a", "c", "d", "m", "y", "z"]
array1_rev = reverseString(array1)
print("the reversed string" + str(array1_rev))
