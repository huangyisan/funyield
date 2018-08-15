class Payment:
    def pay(self):
        raise NotImplementedError

class ApplePay(Payment):
    def zhifu(self,money):
        print("ApplePay zhifu %d" % money)

# 必须实现pay方法,否则报错NotImplementedError
    def pay(self):
        print("ApplePay pay")

app = ApplePay()
app.zhifu(200)
#ApplePay必须实现，才调用不报错
app.pay()