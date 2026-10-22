def check_if_exist(arr: list[int]) -> bool:
    n = len(arr)
    
    for i in range(n):
        for j in range(n):
            if i != j and arr[i] == 2 * arr[j]:
                return True
                
    return False


print(check_if_exist([10, 2, 5, 3]))
print(check_if_exist([3, 1, 7, 11]))