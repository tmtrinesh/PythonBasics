class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno  = rollno
        self.lap = self.Laptop()




    def show(self):
        print(self.name,self.rollno,self.lap)

    class Laptop:
        def __init__(self):
            self.brand = 'Dell'
            self.cpu = 'i9'
            self.ram = 8


s1 = Student('Trinesh',2)
s2 = Student('john',4)



s1.show()
#s2.show()
lap1 = s1.lap
lap2 = s2.lap


print(id(lap1))
print(id(lap2))

#print(s2.name,s2.rollno)