class test(object):
    # name = 'huangyisan'
    def __init__(self):
        self.name = 'huangyisan'

    def get_name(self):
        return self.name

man = test()
print(getattr(man, "name"))
print(getattr(man, "get_name"))
print(getattr(man, "get_age",'1'))
print(getattr(man, "get_name")())