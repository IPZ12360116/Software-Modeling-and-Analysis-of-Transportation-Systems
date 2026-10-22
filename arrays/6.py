def remove_duplicates(nums: list[int]) -> int:
    if len(nums) == 0:
        return 0
        
    k = 1 
    
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1
            
    return k

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k = remove_duplicates(nums)
print(k, nums[:k]) 