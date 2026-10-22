def replace_elements(arr: list[int]) -> list[int]:
    right_max = -1
    
    for i in range(len(arr) - 1, -1, -1):
        current = arr[i]
        arr[i] = right_max
        
        if current > right_max:
            right_max = current
            
    return arr


print(replace_elements([17, 18, 5, 4, 6, 1]))
print(replace_elements([400]))