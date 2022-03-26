"""1 . Single Inheritance"""
# the concept of inheriting from one class to another class is known as single inheritance

# class p:
#     def m1(self):
#         print("parent class")
#
# class c(p):
#     def m2(self):
#         print("child class")
#
# c = c()
# c.m2()
# c.m1()


"""2 . MultiLevel Inheritance"""
# The concept of inheriting the properties from multiple class to a single class with the concept of one after another
# is known as multilevel inheritance
#
# class p:
#     def m1(self):
#         print("parent Method")
#
# class c(p):
#     def m2(self):
#         print("child class")
#
# class cc(c):
#     def m3(self):
#         print("Sub child method")
#
# c = cc()
# c.m1()
# c.m2()
# c.m3()

"""3 . Hierarchical inheritance"""
# the concept of inheriting properties from one class into multiple classes which are present at same level
# is known as hierarchical inheritnce

#
# class p:                       # parentsclass
#     def m1(self):
#         print("parent method")
#
# class c1(p):                              # child 1   class
#     def m2(self):
#         print("child_1 method")
#
# class c2(p):                              # child 2  class
#     def m3(self):
#         print("child_2 method")
# print(":::::::::::::child_1::::::::::::::::")
# c1= c1()               # child 1 class object created
# c1.m1()                # m1 method calling
# c1.m2()                # m2 method calling
# print(":::::::::::::child_2::::::::::::::::")
# c2 = c2()              # child 2 class object created
# c2.m1()
# c2.m3()

"""4 . Multiple Inheritance"""
# The concept of inheriting properties from multiple class into a single class at a time ,
# is known as multiple inheritance
#
# class p1:
#     def m1(self):
#         print("parent 1 method ")
#
# class p2:
#     def m2(self):
#         print("parent 2 method ")
#
# class c(p1,p2):
#     def m3(self):
#         print("child method")
# c = c()
# c.m1()
# c.m2()
# c.m3()

"""5 . hybrid inheritance"""
# combination of single , multi level , multiple  and hierarchical inheritance , is known as hybrid inheritance
"""MRO - : Method Resolutiom Order"""
# class A:
#     pass
# class B(A):
#     pass
# class C(A):
#     pass
# class D(B,C):
#     pass
# print(D.mro())
# print(B.mro())
# print(C.mro())
# print(A.mro())

"""Method Resolution Order (MRO)"""
# class A:
#     def m1(self):
#         print("A class method")
#
# class B(A):
#     def m2(self):
#         print("B class method")
#
# class C(A):
#     def m1(self):
#         print("C class method")
#
# class D(B,C):
#     def m4(self):
#         print("D class method")
#
# print(D.mro())
# d = D()
# d.m1()


# class A:
#     def m1(self):
#         print("A class method")
# class B:
#     def m1(self):
#         print("B class method")
# class C:
#     def m1(self):
#         print("C class method")
# class D(A,B):
#     def m2(self):
#         print("D class method")
# class E(B,C):
#     def m1(self):
#         print("E class method")
# class F(D,E,C):
#     pass
#
# f = F()
# f.m1()
#
#
# print(F.mro())                 # F D A E B C Obj

"""[<class '__main__.F'>, <class '__main__.D'>, <class '__main__.A'>, <class '__main__.E'>,
    <class '__main__.B'>, <class '__main__.C'>, <class 'object'>]
"""

#
# class D:
#     pass
# class E:
#     pass
# class F:
#     pass
# class B(D,E):
#     pass
# class C(D,F):
#     pass
# class A(B,C):
#     pass
#
# print(D.mro())   # [<class '__main__.D'>, <class 'object'>]
# print(B.mro())   # [<class '__main__.B'>, <class '__main__.D'>, <class '__main__.E'>, <class 'object'>]
# print(C.mro())   # [<class '__main__.C'>, <class '__main__.D'>, <class '__main__.F'>, <class 'object'>]
# print(A.mro())
"""[<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, 
<class '__main__.E'>, <class '__main__.F'>, <class 'object'>]"""
#===============================================================


#
# class p:
#     def m1(self):
#         print("parent method")
#
# class c(p):
#     def m2(self):
#         self.m1()                      # calling parent class method from child class
#         print("child method")                # if method name is same then we will get RecursionError
#
# c= c()
# c.m2()

""" super() Method """
#super() is in-built method which is usefull to call the super class -
# - constructor , variable, and method from the child class

"""program -1"""
# class p:
#     def m1(self):
#         print("parent method")
#
# class c(p):
#     def m1(self):
#         super().m1()         # if parent and child class contain a member with same name, then we use super()
#         print("child method")
#
# c= c()
# c.m1()

"""program - 2"""
# class p:
#     a = 10
#     def __init__(self):
#         self.b = 20
#
#     def m1(self):
#         print("parents instance method")
#
#     @classmethod
#     def m2(cls):
#         print("parent class method")
#
#     @staticmethod
#     def m3():
#         print("parent static method")
#
# class c(p):
#     a = 888
#     def __init__(self):
#         self.b = 999
#         super().__init__()          # parent class constructor called
#         print(super().a)
#         print(self.b)
#         super().m1()
#         super().m2()
#         super().m3()
# c = c()


"""program 3"""
# class a:
#     def __init__(self, name , age , marks):
#         self.name = name
#         self.age = age
#         self.marks = marks
#
# class b(a):
#     def __init__(self ,name, age, marks, roll , id):
#         super().__init__(name, age, marks)
#         self.roll = roll
#         self.id = id
#
#     def info(self):
#         print("Name : ",    self.name)
#         print("age: ",      self.age)
#         print("marks: ",    self.marks)
#         print("roll_no : ", self.roll)
#         print("id : ",      self.id)
#
# b = b("nafees", 24 , 99, 39 , 1122332211)
# b.info()







"""How to call method  of a  particular  super class"""
# there is 2 approach
"""1 -  classname.methodname()
   2 -  super(classname , self).methodname()
"""

# class A:
#     def m1(self):
#         print("A class method")
# class B(A):
#     def m1(self):
#         print("B class method")
# class C(B):
#     def m1(self):
#         print("C class method")
# class D(C):
#     def m1(self):
#         print("D class method")
# class E(D):
#     def m1(self):
#         A.m1(self)                         # B class , method called ----      classname.methodname()
#
# e = E()
# e.m1()



# class A:
#     def m1(self):
#         print("A class method")
# class B(A):
#     def m1(self):
#         print("B class method")
# class C(B):
#     def m1(self):
#         print("C class method")
# class D(C):
#     def m1(self):
#         print("D class method")
# class E(D):
#     def m1(self):
#         super(D, self).m1()                # it will call m1() method of super class of D
#                                            # super(classname , self).methodname()
#
# e = E()            # E class object created
# e.m1()             # m1() method calling of E class


#
# class p:
#     a= 10
#     def __init__(self):
#         self.b = 20
#
# class c(p):
#     def m1(self):
#         print(super().a)
#         print(self.b)
#
# c = c()
# c.m1()



#
# class p:
#     def __init__(self):
#         print("parent constructor")
#     def m1(self):
#         print("parent instance method ")
#     @classmethod
#     def m2(cls):
#         print("parent class method")
#     @staticmethod
#     def m3():
#         print("parent static mathod")
#
# class c(p):
#     def __init__(self):
#         super().__init__()
#         super().m1()
#         super().m2()
#         super().m3()
#     def m1(self):
#         super().__init__()
#         super().m1()
#         super().m2()
#         super().m3()
# c = c()
# c.m1()


"""from class method of child class , how to call parent class instance method and constructor"""
#
# class A:
#     def __init__(self):
#         print("parent constructor")
#
#     def m1(self):
#         print("parent instance method")
#
# class B(A):
#     @classmethod
#     def m2(cls):
#         super(B, cls).__init__(cls)             # parent class constructor called
#         super(B, cls).m1(cls)                   # parent class instance method called
#
# B.m2()     # class method called by using class name
#


"""how to call parent class static method from child class static method by using super()"""

class A:
    @staticmethod
    def m1():
        print("parent static method")

class B(A):
    @staticmethod
    def m2():
        super(B, B).m1()

B.m2()         # m2 method called by using B class name



















