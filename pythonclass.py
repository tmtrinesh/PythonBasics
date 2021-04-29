class A:

    def __init__(self):
        print("in A init")
    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")


class B(A):
    def __init__(self):
        super().__init__()
        print("in B init")

    def feature3(self):
        print("Feature 3 working")
    def feature4(self):
        print(" Feature 4 working")

class C(B):
    def feature5(self):
        print("Feature 5 working")

a1 = B()

a1.feature1()
a1.feature2()


b1 = B()
b1.feature3()
b1.feature4()

c1 = C()
c1.feature5()
c1.feature3()
c1.feature4()
c1.feature1()
c1.feature2()