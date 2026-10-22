def duplicate_zeros(arr: list[int]) -> None:
    n = len(arr)
    copy = [x for x in arr] 
    
    read_idx = 0
    write_idx = 0
    
    while write_idx < n:
        arr[write_idx] = copy[read_idx]
        write_idx += 1
        
        if copy[read_idx] == 0 and write_idx < n:
            arr[write_idx] = 0
            write_idx += 1
            
        read_idx += 1


arr1 = [1, 0, 2, 3, 0, 4, 5, 0]
duplicate_zeros(arr1)
print(arr1)

arr2 = [1, 2, 3]
duplicate_zeros(arr2)
print(arr2) 