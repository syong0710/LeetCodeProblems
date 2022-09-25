def threeSum(nums:list, sum:int):
    ans = []
    n = len(nums)
    nums.sort()
    for i in range(n):
        left = i + 1
        right = n - 1
        if nums[i] > sum:
            break
        if i >= 1 and nums[i] == nums[i - 1]:
            continue
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total > sum:
                right -= 1
            elif total < sum:
                left += 1
            else:
                ans.append([nums[i], nums[left], nums[right]])
                while left != right and nums[left] == nums[left + 1]: left += 1
                while left != right and nums[right] == nums[right - 1]: right -= 1
                left += 1
                right -= 1
    return ans

input_nums = [-1, 0, 1, 2, -1, -4]
#target_sum = 3
target_sum = 0

nums_3Sum = threeSum(input_nums, target_sum)

print("The target sum = " + str(target_sum) + "; The three elements: " + str(nums_3Sum))