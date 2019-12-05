def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} == {1}".format(key, value))


output={'name':'yisan'}
greet_me(name="yasoob")
greet_me(**output)
