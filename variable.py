"""1. instance variable(object level variable)
2. static variable(class level variable)
3. local variable
"""

# 1. instance variable(object level variable)
"""instance variable is decelered inside the constructor , inside the instance method and outside the class"""
class test:
    def __init__(self):
        self.a= 10              # instance variable
        self.b= 20

t= test()
print(t.__dict__)

# ============================
# class test:
#     def __init__(self):
#         self.a=10
#         self.b= 30
#     def m1(self):
#         self.c= 40        # self.c  instance variable  will be added in object once we call method
#
#
# t= test()
# t.m1()                  #  m1() method calling
# print(t.__dict__)        # .__dict__ -->> to check how many key and value present in object (return in dict type)
#==================================
# class test:
#     def __init__(self):
#         self.a=10
#         self.b=20
#
#     def m1(self):
#         self.c= 40
#
# t=test()       # object created , constructor called .....  a,b will be added to object
# t.m1()         # instance method calling , c will added to object
# t.d= 50        # d will added to object     (instance variable created by using reference variable)
# print(t.__dict__)
#===========================================

# class test:
#     def __init__(self):
#         self.a=10
#         self.b=20
#
#     def m1(self):
#         self.c= 40
#
# t=test()       # object created , constructor called .....  a,b will be added to object
# t.m1()         # instance method calling , c will added to object
# t.d= 50        # d will added to object     (instance variable created by using reference variable)

# t2= test()
# print("t1 object: ",t.__dict__)
# print("t2 object: ",t2.__dict__)
#==========================================
#
# class  Test:
#     def __init__(self):
#         self.a= 10
#         self.b= 20
#         self.c= 30
#         self.d= 40
#
#     def m1(self):
#         del self.c           # instance variable  deleted
#
#
# t= Test()                #  object created
# print(t.__dict__)
#
# t.m1()                         # m1()  instance method calling
# print(t.__dict__)
#
# t2= Test()
# del t2.b, t2.d
# print(t2.__dict__)
# =========================================
#
# class test:
#     def __init__(self):
#         self.a= 888
#         self.b= 999
#
# t1= test()
# t1.a= 10
# t1.b= 20
#
# t2 = test()
# print("t1.object: ",t1.a, t1.b)
# print("t2 object: ",t2.a,t2.b)
"""====================================================="""


# 2. static variable(class level variable)
"""if the value of a variable is not varried from object to object,  
declare within the class directly but outside of method"""

# class Test():
#     a= 10                 # static variable
#     def __init__(self):
#         Test.b= 20                # static variable inside constructor using class name only
#
#     def m1(self):
#         Test.c= 40                # static variable  inside instance method by using class name only
#
#     @classmethod
#     def m2(cls):
#         cls.d= 22                # static variable inside class method by using cls or class name
#         Test.e= 11
#
#     @staticmethod
#     def m3():
#         Test.f= 50               # static variable inside static method by using class name,
#
# t1= Test()
# t1.m1()             # instance method calling
# Test.m2()           # class method calling
# Test.m3()           # static method calling  ,  it is not related with object
#
# Test.g= 70     # static variable , outside of the  class
# print(Test.__dict__)     # to check static Variable
#================================================================
#
# class Test:
#     x= 10                # static variable
#     def __init__(self):
#         self.y= 20
#
# t1= Test()
# t2= Test()
#
# print("t1 obj: ", Test.x, t1.y)
# print("t2 obj: ", t2.x, t2.y)
#
# print()
# Test.x= 888            #for total class only one copy of static variable will be created and shared by all object
# t1.y= 999
# print("t1 obj: ", Test.x,t1.y)
# print("t2 obj: ", Test.x, t2.y)
#==========================================================
#How to access static variable
# class test:
#     a=10
#     def __init__(self):
#         print(self.a)
#         print(test.a)
#     def m1(self):
#         print(self.a)
#         print(test.a)
#
#     @classmethod
#     def m2(cls):
#         print(cls.a)
#         print(test.a)
#
#     @staticmethod
#     def m3():
#         print(test.a)
#
# t1= test()
# t1.m1()
# test.m2()
# test.m3()
#
# print(t1.a)
# print(test.a)
# ==================================================

# where we can modify the value of static variable
"""we can modify the value by using class name only,  but inside the class method we can use class name or cls"""
# class Test:
#     a=10
#     def __init__(self):
#         Test.a= 20                # value of static variable is modified automatically when object created
#
#     def m1(self):
#         Test.a= 30
#
#     @classmethod
#     def m2(cls):
#         cls.a= 40
#         Test.a= 50
#
#     @staticmethod
#     def m3():
#         Test.a= 60
# print(Test.a)
#
# t= Test()                 # object  created
# print(Test.a)
#
# t.m1()
# print(Test.a)
#
# Test.m2()
# print(Test.a)
#
# Test.m3()
# print(Test.a)
#
# Test.a= 70
# print(Test.a)
#----------------------------------------------
# class test:
#     a=10                # static variable
#     def m1(self):
#         self.a=30         # instance variable
#
# t= test()
# t.m1()
#
# print(test.a)
# print(t.a)
#################################################
# class test:
#     a=10                      # static variable
#     def m1(self):
#         test.a= 888           # static variable
#
# t= test()
# t.m1()
#
# print(test.a)          # 888
# print(t.a)             # 888
#####################################################

# class test:
#     a=10
#     def __init__(self):
#         self.b= 20
#
# t1= test()
# t2= test()
# print(t1.a, t1.b)        #  10, 20
# print(t2.a, t2.b)         # 10, 20
#
# t1.a= 888                 # instance variable created inside t1 object
# t1.b= 999
# print(t1.a, t1.b)         # 888, 999
# print(t2.a, t2.b)         # 10, 20
########################################################

# class test:
#     a= 10
#     def __init__(self):
#         self.b= 20
#
# t1= test()
# t2= test()
#
# print(t1.a ,t1.b)
# print(t2.a, t2.b)
#
# test.a = 888
# test.b = 999                   # static variable created within the class
# print(t1.a , t1.b)
# print(t2.a, t2.b)
# print(test.a, test.b)
########################################################
# class test:
#
#     a= 10
#     def __init__(self):
#         self.b= 20
#
# t1= test()
# t2= test()
#
# test.a= 888
# t1.b= 999
#
# print(t1.a, t1.b)
# print(t2.a, t2.b)
# #=================================================
#
# class test:
#
#     a= 10
#     def __init__(self):
#         self.b= 20
#
#     def m1(self):
#         self.a= 888
#         self.b= 999
#
# t1= test()
# t2= test()
#
# t1.m1()
#
# print(t1.a, t1.b)
# print(t2.a, t2.b)
#***************************************************
#
# class test:
#
#     a= 10
#     def __init__(self):
#         self.b= 20
#
#     @classmethod
#     def m1(cls):
#         cls.a= 888
#         cls.b= 999
#
# t1= test()          # object created
# t2= test()
#
# t1.m1()             # class method calling
#
# print(t1.a, t1.b)            # 888, 20
# print(t2.a, t2.b)            # 888, 20
# print(test.a, test.b)        # 888, 999

#====================================================

""" How to delete  static variable of a class"""
#
# class test:
#     a= 10
#
#     @classmethod
#     def m1(cls):
#         del cls.a
#
# test.m1()
#print(test.__dict__)

########################################################################################
# we can modify or delete static variable only by using classname or cls variable...

# class test:
#     a= 10
#
#     def __init__(self):
#         test.b= 20
#         del test.a
#
#     def m1(self):
#         test.c= 30
#         del test.b
#
#     @classmethod
#     def m2(cls):
#         cls.d= 40
#         del test.c        # del  cls.c
#
#     @staticmethod
#     def m3():
#         test.e= 50
#         del test.d
#
# print(test.__dict__)
# t= test()
#
# print(test.__dict__)
# t.m1()
#
# print(test.__dict__)
# t.m2()
#
# print(test.__dict__)
# t.m3()
#
# print(test.__dict__)
#
# test.f= 60
# print(test.__dict__)
#
# del test.e
#
# print(test.__dict__)              #  'f': 60
#
"""=========================================================="""

"""# Local variable   or Temproary variable

# local variable will be created at the time of method execution and destroyed one method complete
# local variable of a method can not be accessed from outside of method
#"""
# class test:
#
#     def m1(self):
#
#         a= 1000
#         print(a)
#
#     def m2(self):
#         b= 2000
#         print(b)
#
# t= test()
# t.m1()       # 1000
# t.m2()       # 2000

#===========================================
#
# class test:
#
#     def m1(self):
#
#         a= 1000
#         print(a)
#
#     def m2(self):
#         b= 2000
#         print(a)          # NameError: name 'a' is not defined
#         print(b)
#
# t= test()
# t.m1()            # 1000
# t.m2()            # 2000
#
"""Local variable of a method can not be accessed from outside of method"""

# class Test:
#
#      @staticmethod
#      def average(list):
#         result= sum(list)/len(list)          # local variable
#         print(result)
#
#
# t= Test()                # object created
# list= [10,20,30,40]
# t.average(list)          # static method calling  by using obj reference
#
#
# class name:
#
#     @staticmethod
#     def m1(name):
#         for x in range(10):                               # x is local variable
#             print("Hello..good morning: ", x, name)
#
# name.m1('nafees')             # static method calling by using class name
#




















