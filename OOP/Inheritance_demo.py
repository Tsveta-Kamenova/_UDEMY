class Person:
    def __init__(self, name):
        self.name = name

    def getname(self):
        return self.name


class employee(Person):
    def isemployee(self):
        return True


obj_emp = employee("Andy")
print(obj_emp.getname())
print(obj_emp.isemployee())