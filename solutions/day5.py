def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(cons1):
    def first(a, b):
        return a
    return cons1(first)

def cdr(cons1):
    def second(a, b):
        return b
    return cons1(second)

def mult(cons1):
    def mult(a, b):
        return a**b
    return cons1(mult)


cons1 = cons(3, 4)
assert car(cons1) == 3
assert cdr(cons1) == 4
print(mult(cons1))
