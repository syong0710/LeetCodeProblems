#qickSort in Python

def quicksort(leftPointer, rightPointer, nums):
    if len(nums) == 1:  # Terminating Condition for recursion. VERY IMPORTANT!
        return nums
    if leftPointer < rightPointer:
        # It looks like the pre-order binary tree traversal ;-)
        pivotPointer = partition(leftPointer, rightPointer, nums) # (process the current tree node)
        quicksort(leftPointer, pivotPointer-1, nums)  # Recursively sorting the left values (search the left child)
        quicksort(pivotPointer+1, rightPointer, nums)  # Recursively sorting the right values (search the right child)
    return nums


def partition(leftPointer, rightPointer, nums):
    # First element will be the pivot
    pivotValue = nums[leftPointer]
    while(leftPointer < rightPointer):
        # keep finding the element smaller than the pivot
        while(leftPointer<rightPointer and nums[rightPointer]>=pivotValue ):
            rightPointer = rightPointer -1
        # the element smaller than the pivot is moved from the right side to the left side
        nums[leftPointer] = nums[rightPointer]
        # keep finding the element larger than the pivot
        while(leftPointer<rightPointer and nums[leftPointer]<=pivotValue ):
            leftPointer = leftPointer +1
        # the element larger than the pivot is moved from the left side to the right side
        nums[rightPointer] = nums[leftPointer]
    # put the pivot to the place where the left pointer and right pointer meet
    nums[leftPointer] = pivotValue
    return leftPointer


example = [49, 38, 65, 97, 76, 13, 27, 49]
print("The input array: " + str(example))
print("The sorted array: " + str(quicksort(0, len(example) - 1, example)))



# The tree plot of the quick sort
#input: 49, 38, 65, 97, 76, 13, 27, 49
#
#                  49                       1st layer
#     <27 38 13 >       <  76 97 65 49>
#         /                  \
#        27                  76             2nd layer
#      <13  38>         <49 65  97>
#      /     \            /      \
#    13       38         49       97        3rd layer
#                           <65>
#                             \
#                             65            4th layer
