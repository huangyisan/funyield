def test():
    print("generator start")
    n = 1
    while True:
        #  这里分两段，yield n先执行后返回内容。等下一次调用的时候，才进行赋值。
        yield_expression_value = yield n
        print("yield_expression_value = %d" % yield_expression_value)
        n += 1


# ①创建generator对象
generator = test()
print(type(generator))

print("\n---------------\n")

# ②启动generator
next_result = generator.__next__()
print("next_result = %d" % next_result)

print("\n---------------\n")

# ③发送值给yield表达式，直接给yield_expression_value赋值为666
send_result = generator.send(666)
print("send_result = %d" % send_result)
