import time


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
t1 = time.time()
print(naive(word1, s1))
print(time.time() - t1)
print('---')

def linear(word, s):
    freq = {}
    ans = []

    for c in word:
        if c not in freq:
            freq[c] = 0
        freq[c] += 1

    for c in s[:len(word)]:
        if c in freq:
           freq[c] -= 1
           if freq[c] == 0:
               del freq[c]

    if not freq:
        ans.append(0)

    for i in range(len(word), len(s)):
        end = i - len(word)

        if s[end] not in freq:
            freq[s[end]] = 0
        freq[s[end]] += 1
        if freq[s[end]] == 0:
            del freq[s[end]]
        
        if s[i] not in freq:
            freq[s[i]] = 0
        freq[s[i]] -= 1
        if freq[s[i]] == 0:
            del freq[s[i]]

        if not freq:
            ans.append(end + 1)

    return ans


t1 = time.time()
print(linear(word1, s1))
print(time.time() - t1)
print('---')
