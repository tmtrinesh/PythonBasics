class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2


    def __add__(self, other):
        m1 = self.m1 +other.m1
        m2 = self.m2 +other.m2
        s3 = Student(m1,m2)

        return s3


s1 = Student(119,69)
s2 = Student(60,65)


s3 = s1 + s2

if s1.m1 > s2.m1:
    print ("s1 wins")
else:
    print("s2 wins")
print(s3.m1)
print(s3.m2)


a=2
b=3
c = a&b
print(c)


print()
