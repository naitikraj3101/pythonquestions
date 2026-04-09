class test:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def showinfo(self):
        return self.name , self.__age
    

obj = test('naitik',20)
print(obj.showinfo())