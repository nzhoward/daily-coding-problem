def naive(word, s):
    ans = []
    for i in range(len(s) - len(word) + 1):
        window = s[i: i + len(word)]
        if is_anagram(window, word):
            ans.append(i)
    return ans
    

def is_anagram(this, other):
    return sorted(this) == sorted(other)


word1 = 'ab'
s1 = 'abxaba'
print(naive(word1, s1))


def linear(word, s):
    freq = {}
    ans = []
    for c in word:
        if c not in freq:
            freq[c] = 0
        freq[c] += 1
    print(freq)
    for i in range(len(s)):
        if s[i] in freq:
            freq[s[i]] -= 1
            if freq[s[i]] == 0:
                del freq[s[i]]
        if not freq:
            ans.append(i)
    print(ans)


linear(word1, s1)
