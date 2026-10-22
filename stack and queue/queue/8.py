def constrained_subset_sum(nums, k):
    n = len(nums)
    dp = [0] * n
    q = []
    head = 0
    max_sum = nums[0]

    for i in range(n):
        while head < len(q) and q[head] < i - k:
            head += 1
        best_prev = dp[q[head]] if head < len(q) and dp[q[head]] > 0 else 0
        dp[i] = nums[i] + best_prev
        if dp[i] > max_sum:
            max_sum = dp[i]
        while head < len(q) and dp[q[-1]] <= dp[i]:
            q.pop()
        q.append(i)

    return max_sum

print(constrained_subset_sum([10, 2, -10, 5, 20], 2))
print(constrained_subset_sum([-1, -2, -3], 1))
print(constrained_subset_sum([10, -2, -10, -5, 20], 2))