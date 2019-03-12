num = 100
def a():
    # num = 100
    def b():
        # nonlocal num
        global num
        num += 1
        print(num)
    return b

demo = a()
demo()
demo()