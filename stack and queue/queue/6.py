def moves_to_stamp(stamp, target):
    s_len = len(stamp)
    t_len = len(target)
    target_list = list(target)
    res = []
    visited = [False] * (t_len - s_len + 1)
    stars = 0

    def can_replace(pos):
        has_char = False
        for i in range(s_len):
            if target_list[pos + i] == '?':
                continue
            if target_list[pos + i] != stamp[i]:
                return False
            has_char = True
        return has_char

    while stars < t_len:
        replaced = False
        for i in range(t_len - s_len + 1):
            if not visited[i] and can_replace(i):
                for j in range(s_len):
                    if target_list[i + j] != '?':
                        target_list[i + j] = '?'
                        stars += 1
                visited[i] = True
                replaced = True
                res.append(i)
                if stars == t_len:
                    break
        if not replaced:
            return []

    return res[::-1]

print(moves_to_stamp("abc", "ababc"))
print(moves_to_stamp("abca", "aabcaca"))