def funca(b,c,a):
    a = a
    b = b
    c = c
    print("funca a is {0}".format(a))
    print("funcb b is {0}".format(b))
    print("funcc c is {0}".format(c))
    print("\n")

    funcb(c=c,b=b)

def funcb(b,c):
    # print("funcb a is {0}".format(a))
    print("funcb b is {0}".format(b))
    print("funcb c is {0}".format(c))

funca(b=2,c=3,a=1)
