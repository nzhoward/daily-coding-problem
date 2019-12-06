def id_to_short(the_id):
    short = ''
    chars = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    tmp = the_id
    while tmp > 0:
        short += chars[tmp % 62]
        tmp = int(tmp / 62)
    short = short[::-1]
    print('ID ' + str(the_id) + ' maps to ' + short)
    return short

def short_to_id(short):
    chars = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    the_id = 0
    for e in list(short):
        tmp = chars.index(e)
        the_id = the_id * 62 + tmp
    print(short + ' maps to ID ' + str(the_id))
    return the_id


id1 = 345321
short_to_id(id_to_short(id1))
