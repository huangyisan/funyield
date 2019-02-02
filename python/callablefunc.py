class Persion(object):
    def __init__(self):
        self.name = 'huangyisan'
        self.age = 28

    def get_name(self):
        print(self.name)

    def __call__(self, *args, **kwargs):
        return self.get_name()

persion = Persion()()
