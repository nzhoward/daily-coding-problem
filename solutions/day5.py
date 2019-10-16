def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(cons):
    def first(a, b):
        return a
    return cons(first)

def cdr(cons):
    def second(a, b):
        return b
    return cons(second)

def mult(cons):
    def mult(a, b):
        return a**b
    return cons(mult)


assert car(cons(3, 4)) == 3
assert cdr(cons(3, 4)) == 4
print(mult(cons(3, 4)))
