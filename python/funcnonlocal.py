def tester(start):
    state = start
    def nested(label):
        print(label,state)
    return nested


if __name__ == '__main__':
    F = tester(0)
    print(F.__name__)
    F('spam')
    F('ham')