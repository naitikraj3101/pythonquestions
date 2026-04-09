class test:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showinfo(self):
        return self.name , self.age
    
class something(test):
    def setname(self,name):
        self.name = name


obj = something('something',20)
print(obj.showinfo())
obj.setname('naitik')
print(obj.showinfo())