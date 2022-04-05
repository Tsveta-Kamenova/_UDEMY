class A:
    def dA(self):
        print("A class Method")


class B(A):
    def dB(self):
        print("B class Method")


class C(A):
    def dC(self):
        print("C class Method")


obj = C()
obj1 = B()

obj.dA()
obj.dC()

obj1.dA()
obj1.dB()