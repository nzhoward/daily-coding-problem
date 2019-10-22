dic_1 = set(['dog', 'deer', 'deal', 'dear', 'donut', 'cat', 'cake', 'boy', 'man', 'mouse', 'map', 'monster', 'dealing'])
lookup_1 = 'd'
lookup_2 = 'do'
lookup_3 = 'de'
lookup_4 = 'deal'
lookup_5 = 'm'
lookup_6 = 'ma'
lookup_7 = 'mo'
lookup_8 = 'gg'


class AutoComplete:
    def __init__(self, dic):
        self.dic = dic
        self.idx = build_idx(dic)

    def lookup(self, lookup):
        if lookup in self.idx.keys():
            return self.idx[lookup]
        else:
            ret = []
            for i in self.dic:
                if i[0: len(lookup)] == lookup:
                    ret.append(i)
            return ret


def build_idx(the_dic):
    idx = {}
    for word in the_dic:
        if len(word) >= 3:
            three = word[0: 3]
            if three not in idx.keys():
                idx[three] = []
            idx[three].append(word)
        if len(word) >= 2:
            two = word[0: 2]
            if two not in idx.keys():
                idx[two] = []
            idx[two].append(word)
        if len(word) >= 1:
            one = word[0: 1]
            if one not in idx.keys():
                idx[one] = []
            idx[one].append(word)

    return idx


ac = AutoComplete(dic_1)
print(ac.idx)
print(lookup_1, ac.lookup(lookup_1))
print(lookup_2, ac.lookup(lookup_2))
print(lookup_3, ac.lookup(lookup_3))
print(lookup_4, ac.lookup(lookup_4))
print(lookup_5, ac.lookup(lookup_5))
print(lookup_6, ac.lookup(lookup_6))
print(lookup_7, ac.lookup(lookup_7))
print(lookup_8, ac.lookup(lookup_8))
