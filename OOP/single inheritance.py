class A:
    def dA(self):
        print("A class Method")


class B(A):
    def dB(self):
        print("B class Method")


obj = B()
obj.dA()
obj.dB()