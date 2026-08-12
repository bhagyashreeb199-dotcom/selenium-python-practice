#acuring properties of parent class
#
from Class_Demo import Calculator


class Inheritance_demo(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 2,10)

    def completeData(self):
        return self.num2 + self.num + self.numberSum()

obj = Inheritance_demo()
print(obj.completeData())