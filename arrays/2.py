def find_numbers(nums: list[int]) -> int:
    even_digits_count = 0
    
    for num in nums:
        digits = 0
        temp = num
        

        while temp > 0:
            digits += 1
            temp //= 10
            
        if digits % 2 == 0:
            even_digits_count += 1
            
    return even_digits_count


print(find_numbers([12, 345, 2, 6, 7896]))
print(find_numbers([555, 901, 482, 1771]))