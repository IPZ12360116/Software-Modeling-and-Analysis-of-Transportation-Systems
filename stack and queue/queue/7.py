def max_sliding_window(nums, k):
    res = []
    q = []
    head = 0

    for i in range(len(nums)):
        while head < len(q) and q[head] <= i - k:
            head += 1
        while head < len(q) and nums[q[-1]] <= nums[i]:
            q.pop()
        q.append(i)
        if i >= k - 1:
            res.append(nums[q[head]])

    return res

print(max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))
print(max_sliding_window([1], 1))