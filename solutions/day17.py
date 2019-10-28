def get_deepest(dir_string):
    dir_list = dir_string.split('\n')
    path = ''
    for i in range(len(dir_list)):
        depth = dir_list[i].count('\t')
        word_i = dir_list[i]
        if '.' in word_i:
            tmp_path = ''
            tmp_path = word_i + tmp_path
            for j in range(depth - 1, -1, -1):
                brk = False
                for k in range(i - 1, -1, -1):
                    if brk is False:
                        depth_k = dir_list[k].count('\t')
                        word_k = dir_list[k]
                        if depth_k == j:
                            tmp_path = word_k + '/' + tmp_path
                            brk = True

            if len(tmp_path) > len(path):
                path = tmp_path
    path = path.replace('\t', '')
    return path, len(path)


dir_string1 = 'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext'
dir_string2 = 'dir\n\tsubdir1\n\tsubdir2\n\t\t\t'
dir_string3 = 'dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext'
dir_string4 = ''
dir_string5 = 'hello.ext'

print(get_deepest(dir_string1))
print(get_deepest(dir_string2))
print(get_deepest(dir_string3))
print(get_deepest(dir_string4))
print(get_deepest(dir_string5))
