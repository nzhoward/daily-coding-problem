def justify_text(words, k):
    length = 0
    for w in words:
        length += len(w)
        if w != words[-1]:
            length += 1
    num_lines = int(length / k) + (length % k > 0)

    idx = 0
    ans = []
    
    for i in range(num_lines):
        temp_word = ''
        end_of_line = False
        temp_line = []
        while not end_of_line:
            if idx <= len(words) - 1 and len(temp_word) + 1 + len(words[idx]) <= k:
                temp_word += words[idx]
                temp_word += ' '
                temp_line.append(words[idx])
                idx += 1
            else:
                end_of_line = True
                temp_word = temp_word[:-1]

        line_length = 0
        for w in temp_line:
            line_length += len(w)

        end_of_line = False
        
        while not end_of_line:
            for i in range(len(temp_line)):
                if line_length + 1 <= k:
                    if len(temp_line) == 1 or i < len(temp_line) - 1:
                        temp_line[i] += ' '
                        line_length += 1
                else:
                    end_of_line = True

        temp_word = ''
        for w in temp_line:
            temp_word += w
        ans.append(temp_word)
    return ans


words1 = ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog', 'very_long_word']
k1 = 16

print(justify_text(words1, k1))
