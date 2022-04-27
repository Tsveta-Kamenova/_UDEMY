class MyClass:
    __var = 67

    def fun(self):
        self.__var += 2
        print(self.__var)


obj = MyClass()
obj.fun()