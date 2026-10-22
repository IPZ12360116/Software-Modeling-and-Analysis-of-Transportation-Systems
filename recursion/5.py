def my_pow(x: float, n: int) -> float:
    if n == 0:
        return 1.0
    
    if n < 0:
        return 1.0 / my_pow(x, -n)
    
    half = my_pow(x, n // 2)
    
    if n % 2 == 0:
        return half * half
    else:
        return half * half * x


# Перевірка:
print(f"{my_pow(2.00000, 10):.5f}") 
print(f"{my_pow(2.10000, 3):.5f}")   
print(f"{my_pow(2.00000, -2):.5f}") 