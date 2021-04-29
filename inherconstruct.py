class A:
    def __init__(self):
        print("constructor from A")
class B(A):
   def __init__(self):
       print("Constructor from B")
       super().__init__()
       A.__init__(self)
bobj =B()


class Myclass():
    def m1(self):
        print("Good Morning")

    def __init__(self):
        print("this is constructor")

c=Myclass()
c.m1()


