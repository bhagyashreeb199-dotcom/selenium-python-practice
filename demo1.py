class Calc:
    num = 100

    def __init__(self, a, b):
        self.firstn = a
        self.secondn = b
        print("auto called")

    def callData(self):
        print("inside the method")

    def summation(self):
        return self.firstn + self.secondn + self.num



obj = Calc(2,5)
obj.callData()
print(obj.summation())

obj1 = Calc(6,7)
obj1.callData()
print(obj1.summation())