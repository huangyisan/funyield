class judge(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print(self):
        print(self.a)
        print(self.b)

    @staticmethod
    def compare(a,b):
        if a > b:
            return True


a = 3
b = 2
# if judge.compare(a, b):
#     test = judge(a, b)
#     test.print()
# else:
#     print('a < b')

test = judge(a,b)
if test.compare(a,b):
    print(1)
else:
    print(2)