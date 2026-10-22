def sorted_squares(nums: list[int]) -> list[int]:
    n = len(nums)
    result = [0] * n
    
    left = 0
    right = n - 1
    pos = n - 1 
    
    while left <= right:
        left_sq = nums[left] * nums[left]
        right_sq = nums[right] * nums[right]
        
        if left_sq > right_sq:
            result[pos] = left_sq
            left += 1
        else:
            result[pos] = right_sq
            right -= 1
            
        pos -= 1
        
    return result


print(sorted_squares([-4, -1, 0, 3, 10]))  
print(sorted_squares([-7, -3, 2, 3, 11])) 