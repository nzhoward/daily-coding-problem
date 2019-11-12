def encode(word):
    cnt = 0
    ans = ''
    for i in range(len(word)):
        if i == 0:
            cnt += 1
            continue
        if word[i] == word[i - 1]:
            cnt += 1
        else:
            ans += (str(cnt) + word[i - 1])
            cnt = 1

    ans += (str(cnt) + word[-1])

    return ans


word1 = 'AAAABBBCCDAA'
word2 = 'ABCDE'
word3 = 'AAAABBBBCCCCDD'
print(encode(word1))
print(encode(word2))
print(encode(word3))
