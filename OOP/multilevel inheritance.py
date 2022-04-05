class A:
    def dA(self):
        print("A class Method")


class B:
    def dB(self):
        print("B class Method")


class C(A, B):
    def dC(self):
        print("C class Method")


obj = C()
obj.dA()
obj.dB()
obj.dC()