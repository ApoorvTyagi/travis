class Arithmatic:
    def __init__(self,value1,value2):
        self.num1=value1
        self.num2=value2

    def add(self,num1,num2):
        return self.num1+num2

    def sub(self):
        return self.num1-self.num2

    def multiply(self,num1,num2):
        return num1*self.num2

    def divide(self):
        return int(self.num1/self.num2)

obj=Arithmatic(10,5)
print(obj.add(15,10))
print(obj.sub())
print(obj.multiply(2,3))
print(obj.divide())
