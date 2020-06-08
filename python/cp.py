class A(object):
    def __init__(self,name):
        self.name = name

    def print_name(self):
        print(self.name)


personA = A('cat')
personB = A('dog')

print(personA.print_name == personB.print_name)

