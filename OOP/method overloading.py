class student:
    def disp(self, roll, name):
        print(roll, name)

    def disp(self):
        print("Welcome")


obj = student()
obj.disp()


# obj.disp(23, "Alex")


class overload:

    def fun(self, a, b=None):
        print(a)

    def fun(self, a, b=None):
        print(a, b)


obj=overload()
obj.fun(89)
obj.fun(23, 45)
