def longest_substring_palindrome(word):
    n = len(word)

    dp = [[0 for x in range(n)] for y in range(n)]
    
    max_len = 1
    i = 0
    while i < n:
        dp[i][i] = True
        i += 1

    start = 0
    i = 0
    while i < n - 1:
        if word[i] == word[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2
        i += 1

    k = 3
    while k <= n:
        i = 0
        while i < n - k + 1:
            j = i + k - 1
            if dp[i + 1][j - 1] and word[i] == word[j]:
                dp[i][j] = True
                
                if k > max_len:
                    start = i
                    max_len = k
            i += 1
        k += 1
    return word[start:start + max_len]

word1 = 'aabcdcb'
print(longest_substring_palindrome(word1))


'''
| |a|a|b|c|d|c|b|
|a|1|0|0|0|0|0|0|
|a|0|1|0|0|0|0|0|
|b|0|0|1|0|0|0|0|
|c|0|0|0|1|0|0|0|
|d|0|0|0|0|1|0|0|
|c|0|0|0|0|0|1|0|
|b|0|0|0|0|0|0|1|

| |a|a|b|c|d|c|b|
|a|1|1|0|0|0|0|0|
|a|0|1|0|0|0|0|0|
|b|0|0|1|0|0|0|0|
|c|0|0|0|1|0|0|0|
|d|0|0|0|0|1|0|0|
|c|0|0|0|0|0|1|0|
|b|0|0|0|0|0|0|1|

| |a|a|b|c|d|c|b|
|a|1|1|0|0|0|0|0|
|a|0|1|0|0|0|0|0|
|b|0|0|1|0|0|0|1|
|c|0|0|0|1|0|1|0|
|d|0|0|0|0|1|0|0|
|c|0|0|0|0|0|1|0|
|b|0|0|0|0|0|0|1|
'''
