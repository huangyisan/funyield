def is_odd(x):
    return x % 2 == 1


print(list(filter(is_odd,[1,2,3,4,5])))

def not_empty(s):
    return s

print(not_empty(' ') is ' ')

print(' ' and ' '.strip())


def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))
