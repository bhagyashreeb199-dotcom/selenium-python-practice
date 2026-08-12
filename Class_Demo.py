#classes are user defined blueprint or prototype and will have methods class,
# instance variable  constructor etc

#__init__ is a keyword to declare constructor
# to call any variable inside your method, you have to always call with <self.>




class Calculator:  # class
    num = 100

    def __init__(self, a, b):
        self.a = a
        self.b = b
        print("Automatic call")

    def getData(self):  # method
        print("Executing method in class")

    def numberSum(self):
        return self.a + self.b

obj = Calculator(4, 7) #syntax to create object in python
obj.getData()
print(obj.numberSum())