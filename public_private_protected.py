"""public , private , protected"""
#
"""public"""

# class p:
#     def __init__(self):
#
#         self.all = 10
#
#
#     def public(self):
#         self.x = 10
#         self.y = 20
#
# a = p()            # object created
# print(a.all)
#
# a.public()
# print(a.y)

#♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦
"""private"""
# private attribute can be accessed only within the class  ...
#  i.e... from outside of the class we can not access.
"""we can declare a variable as private explicity by prefexing with 2 __ underscore symbol"""

# class Test:
#     __x = 10
#     __y = 20
#     __z = 30
#     def m1(self):
#         print(Test.__x)           # from inside the class we can access
#
# t = Test()
# t.m1()
# print(Test.__x)             # from outside of the class we can not access.
# print(Test.__y)             # AttributeError: 'Test' object has no attribute '__y'
# print(Test.__z)               # AttributeError: type object 'Test' has no attribute '__z'


""" How we can access private variable from outside of the class """
# we can not access private variable directly from outside of the class

"""__variablename , internally name mangling will be happen , and new name allocated i.e. _classname__variablename """
# but we can access indirectly as follow:
""" ObjectReference._classname__variablename """

class Test:
    def __init__(self):
        self.__x = 10

t = Test()
print(t._Test__x)


#♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦

"""protected"""

# protected attributes can be accessed within the class anywhere but from outside of the class only in child class ,
# we can specify attribute as protected by prefexing with _ symbol

"""
_name = "nafees"
"""

# but it is just conventional and in reality does not exist protected attributes






















