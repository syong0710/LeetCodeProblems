from collections import deque
def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    length = len(nums)
    result = []
    que = deque()
    for i in range(length):
        # 在加入新数字前，弹出所有比当前值小的数字
        # 以确保加入后的单调递减性
        while que and nums[que[-1]] < nums[i]:
            que.pop()
        # 上面的循环完成后，加入新数字
        que.append(i)
        # 如果当前要被淘汰的数字nums[i-k]是双端队列的左端点
        # 即说明，当前最大值过期要被淘汰掉，从左侧弹出队列
        if i >= k and que[0] == i - k:
            que.popleft()
        # 一旦窗口内元素达到K个，就开始计算滑动最大值
        # 最大值永远是单点递减双端队列的左端点
        if i >= k - 1:
            result.append(nums[que[0]])
    return result

input_nums = [1, 3, -1, -3, 5, 3, 6, 7] # The input array
input_k = 3 # The size of the window

max_list = maxSlidingWindow(input_nums, input_k)
print(max_list)

