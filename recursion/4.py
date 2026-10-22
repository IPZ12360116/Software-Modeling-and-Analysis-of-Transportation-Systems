def climb_stairs(n: int, memo: dict = None) -> int:
    if memo is None:
        memo = {}
        
    if n <= 2:
        return n
    
    if n not in memo:
        memo[n] = climb_stairs(n - 1, memo) + climb_stairs(n - 2, memo)
        
    return memo[n]

print(climb_stairs(2))   
print(climb_stairs(3))   
print(climb_stairs(45))  