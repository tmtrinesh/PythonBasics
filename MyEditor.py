


class MyEditor:
    def execute(self):
        print("Spell Check")
        print("Conversion Check")
        print("Compiling")
        print("Running")


class Laptop:
    def code(self,ide):
        ide.execute()


ide = MyEditor()



lap1 =  Laptop()
lap1.code(ide)


a = 5
b = 6
print(a+b)
print(int.__add__(a,b))


a = '5'
b = '87'
print(a+b)
print(str.__add__(a,b))

