def longest_valid_parentheses(s):
    stack = [-1]
    max_len = 0
    
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                curr_len = i - stack[-1]
                if curr_len > max_len:
                    max_len = curr_len
                    
    return max_len

print(longest_valid_parentheses("(()"))
print(longest_valid_parentheses(")()())"))
print(longest_valid_parentheses(""))