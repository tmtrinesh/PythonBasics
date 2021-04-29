class Computer:

    def __init__(self):
        self.name = "jaan"
        self.age = 31
    def updae(self):
        self.age = 30

    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = Computer()
c2 = Computer()

if c1.compare(c2):
    print("They are same")




print(c1.name)
print(c1.age)



c1.name = "Trinesh"
c1.age= 13


print(c1.name)
print(c1.age)



