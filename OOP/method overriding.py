class myclass:

    def fun(self, n1, n2):
        return n1+n2

class child(myclass):

    def fun(self, n1, n2):
        return n1*n2

obj = child()
print(obj.fun(2, 3))

objp = myclass()
print(objp.fun(2,3))