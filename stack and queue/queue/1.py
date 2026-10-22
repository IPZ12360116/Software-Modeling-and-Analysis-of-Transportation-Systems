def first_uniq_char(s):
    counts = {}
    q = []
    
    for i in range(len(s)):
        ch = s[i]
        counts[ch] = counts.get(ch, 0) + 1
        q.append(i)
        
    for idx in q:
        if counts[s[idx]] == 1:
            return idx
            
    return -1

print(first_uniq_char("leopard"))
print(first_uniq_char("loveleopard"))
print(first_uniq_char("aabb"))