def mylist(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
        yield a

print(sum(mylist(100))-1)