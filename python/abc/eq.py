class Person(object):
    def __init__(self, age):
        self.age = age

    def __eq__(self, other):
        if not isinstance(other, Person):
            print('NotImplemented')
            return NotImplemented
        return self.age == other.age

class Age(object):
    def __init__(self, age):
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

person = Person(10)
age = Age(10)
print(person == age)

# print(isinstance(Age, Person))
