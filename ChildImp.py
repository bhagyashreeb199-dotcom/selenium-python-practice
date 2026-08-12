from demo1 import Calc  #import other class, "demo1 is file name in that we are importing "Clas" class


class ChildImp(Calc):
    num2 = 200

    def __init__(self):
        Calc.__init__(self,5,8)

    def getCompleteData(self):
        return self.num2 + self.num +self.summation()

obj = ChildImp()
print(obj.getCompleteData())