def is_balanced(brackets):
    stack = []
    for b in brackets:
        if b == '(' or b == '[' or b == '{':
            stack.append(b)
        if len(stack) > 0 and matches(stack[-1], b):
            del stack[-1]
    print(stack)
    return len(stack) == 0


def matches(a, b):
    if (a == '(' and b == ')') or (a == '[' and b == ']') or (a == '{' and b == '}'):
        return True
    return False


brackets1 = '([])'
brackets2 = '(({[]}))'
brackets3 = '([)]'
brackets4 = '((()'
print(is_balanced(brackets1))
print(is_balanced(brackets2))
print(is_balanced(brackets3))
print(is_balanced(brackets4))
