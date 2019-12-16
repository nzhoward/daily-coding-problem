def find_word(word, word_idx, i, j, mat):
    if i > len(mat) - 1 or j > len(mat[0]) - 1:
        return False
    if word[word_idx] == mat[i][j] and len(word) - 1 == word_idx:
        return True

    if word[word_idx] == mat[i][j]:
        return find_word(word, word_idx + 1, i, j + 1, mat) or find_word(word, word_idx + 1, i + 1, j, mat)
    else:
        return find_word(word, word_idx, i, j + 1, mat) or find_word(word, word_idx, i + 1, j, mat)


mat1 = [['F', 'A', 'C', 'I'],
         ['O', 'B', 'Q', 'P'],
         ['A', 'N', 'O', 'B'],
         ['M', 'A', 'S', 'S']]

word1 = 'FOAM'
word2 = 'MASS'
word3 = 'FOBS'
word4 = 'GONE'
print(find_word(word1, 0, 0, 0, mat1))
print(find_word(word2, 0, 0, 0, mat1))
print(find_word(word3, 0, 0, 0, mat1))
print(find_word(word4, 0, 0, 0, mat1))
