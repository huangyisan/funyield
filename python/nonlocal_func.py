state = 0
def tester(start):
    state = 1
    def cisco(middle):
        pass
        def nested(label):
            nonlocal state
            print(label, state)
        return nested
    return cisco

F=tester(0)
F(1)('spam')