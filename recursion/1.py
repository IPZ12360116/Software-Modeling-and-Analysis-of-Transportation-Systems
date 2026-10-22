def print_reverse(s: str) -> None:
    if len(s) == 0:
        return
    
    print_reverse(s[1:])
    
    print(s[0], end="")

print_reverse("tiger")
print()