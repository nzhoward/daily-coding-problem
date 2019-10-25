def k_unique_substring_linear(s, k):
    a = set()
    p1 = 0
    p2 = 0
    mx = 0
    start = 0
    end = 0

    if len(s) < k:
        return None
    
    while p2 != len(s):
        if len(a) != k:
            a.add(s[p1])
            a.add(s[p2])
            p2 += 1
        elif s[p2] in a:
            p2 += 1
        elif s[p2] not in a:
            a.clear()
            p1 += 1
            a.add(s[p1])
        if p2 - p1 > mx:
            mx = p2 - p1
            start = p1
            end = p2
            
    if len(a) != k:
        return None
    return s[start: end]


s1 = 'abcba'
s2 = 'accccz'
s3 = 'abcdcdcd'
s4 = 'aaacd'
s5 = ''
s6 = 'ab'
k = 3

print(k_unique_substring_linear(s1, k))
print(k_unique_substring_linear(s2, k))
print(k_unique_substring_linear(s3, k))
print(k_unique_substring_linear(s4, k))
print(k_unique_substring_linear(s5, k))
print(k_unique_substring_linear(s6, k))
