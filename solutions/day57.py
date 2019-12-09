def break_up_string(sentence, k):
    words = sentence.split(' ')
    ret = []
    tmp = ''
    for word in words:
        og = '' + tmp
        tmp += word + ' '
        if len(tmp) - 1 <= k:
            continue
        else:
            ret.append(og[0:-1])
            tmp = word + ' '
    ret.append(tmp[0:-1])
    return ret
    

sentence1 = 'the quick brown fox jumps over the lazy dog'
k1 = 10
print(break_up_string(sentence1, k1))


sentence2 = 'a sentenceee with a very lonng word'
k2 = 10
print(break_up_string(sentence2, k2))
