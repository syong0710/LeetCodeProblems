def bubble_sort(nums:list) -> list:
    length = len(nums)
    if nums is None or length<2:
        return nums
    ifSwaped:bool = True
    while ifSwaped is True:
        ifSwaped = False
        for left in range(0, length-1):
            right = left + 1
            if nums[left] > nums[right]:
                nums[left], nums[right] = nums[right], nums[left]
                ifSwaped = True
    return nums


nums1 = [8, 1, 6, 4, 9, 2, 5, 5]
nums1_sorted = bubble_sort(nums1)

print("The input array is " + str(nums1))
print("The sorted array is " + str(nums1_sorted))