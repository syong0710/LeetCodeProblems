# return the final index of the list with the removed elements
def removeElement(nums:list, target:int) -> int:
    if nums is None or len(nums)==0:
        return 0
    left = 0
    right = len(nums)-1
    while left < right:
        while left<right and nums[left]!=target:
            left += 1
        while left<right and nums[right]==target:
            right -=1
        nums[left], nums[right] = nums[right], nums[right]

    if nums[left] == nums[right]:
        return right
    else:
        return left


inputNums = [0, 1, 2, 3, 3, 0, 4, 2]
removeTarget = 2
outputInd = removeElement(inputNums, removeTarget)
print(outputInd)

print("The input array is :" + str(inputNums))
print("The array with the element=" + str(removeTarget) + " is: " + str(inputNums[0:outputInd+1]))
