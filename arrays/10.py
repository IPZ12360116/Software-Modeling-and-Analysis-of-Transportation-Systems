def sort_array_by_parity(nums: list[int]) -> list[int]:
    even_pos = 0
    
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            nums[even_pos], nums[i] = nums[i], nums[even_pos]
            even_pos += 1
            
    return nums


print(sort_array_by_parity([3, 1, 2, 4]))
print(sort_array_by_parity([0]))