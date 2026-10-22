def find_max_consecutive_ones(nums: list[int]) -> int:
    max_count = 0
    current_count = 0
    
    for num in nums:
        if num == 1:
            current_count += 1
            if current_count > max_count:
                max_count = current_count
        else:
            current_count = 0
            
    return max_count


print(find_max_consecutive_ones([1, 1, 0, 1, 1, 1]))
print(find_max_consecutive_ones([1, 0, 1, 1, 0, 1]))