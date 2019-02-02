class Payment:
    money = 100
    def __init__(self):
        self.selfmoney = 100
    def pay(self):
        pass

print(Payment.__dict__)
print(Payment().__dict__)