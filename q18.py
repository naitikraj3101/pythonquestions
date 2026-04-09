class test:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showinfo(self):
        return self.name , self.age
    

obj = test('something',20)
print(obj.showinfo())