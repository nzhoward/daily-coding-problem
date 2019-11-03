def word_break_recur(words, word):
    ans = []
    if word_break_helper(words, word, ans):
        return ans
    else:
        return None


def word_break_helper(words, word, ans):
    if word == '':
        return True
    else:
        for i in range(1, len(word) + 1):
            if word[:i] in words and word_break_helper(words, word[i:], ans):
                ans.append(word[:i])
                return True
        return False

    
words1 = ['the', 'quick', 'brown', 'fox']
word1 = 'thequickbrownfox'

words2 = ['bed', 'bath', 'bedbath', 'and', 'beyond']
word2 = 'bedbathandbeyond'


print(word_break_recur(words1, word1))
print(word_break_recur(words2, word2))
print(word_break_recur(words1, 'hello'))


def word_break_dp(words, word):
    ans = []
    dp = [None] * (len(word) + 1)
    dp[0] = True
    for i in range(len(word) + 1):
        for j in range(i):
            if dp[j] and word[j: i] in words:
                dp[i] = True
                ans.append(word[j: i])
                break
    if len(ans) == 0:
        return None
    return ans
            

print(word_break_dp(words1, word1))
print(word_break_dp(words2, word2))
print(word_break_dp(words1, 'hello'))
