"""Has-A Relationship (by Composition)"""

#
# class Engine:                      # Engine class
#     def __init__(self):
#         self.power = '10KW'
#
#     def useEngine(self):
#         print("Engine specific functionality")
#
# class car:                          # car class
#     def __init__(self):                                # constructor
#         self.engine = Engine()        # Engine object created
#
#     def usecar(self):                                           # instance variable
#         print("car required engine functionality")
#         self.engine.useEngine()                      # calling useEngine instance method
#         print(self.engine.power)
#
# c = car()                 # car object created
# c.usecar()
#===============================================
#
# class engine:
#
#     a =10
#     def __init__(self):
#         self.b = 20
#
#     def m1(self):
#         print("Engine specific functionality")
#
# class car:
#     def __init__(self):
#         self.engine = engine()
#
#     def m2(self):
#         print("car using engine class functionality")
#         print(self.engine.a)
#         print(self.engine.b)
#
#         self.engine.m1()
#
#
# c= car()
# c.m2()
#------------------------------------------------
#
# class car:
#
#     def __init__(self, name , model, color):
#
#         self.name = name
#         self.model = model
#         self.color = color
#
#     def getinfo(self):
#         print("car name : {} , model : {}, and color : {} ".format(self.name , self.model, self.color))
#
# class employee:
#
#     def __init__(self, ename , eno , car ):
#         self.ename = ename
#         self.eno = eno
#         self.car = car
#
#     def empinfo(self):
#         print("Employee name : ", self.ename)
#         print("Employee number : ", self.eno)
#         print("Employee car info : ")
#         self.car.getinfo()                      # instance method calling
#
# c = car("innova" , "2.5V" , "Grey")                 # car object created
#
# e = employee("nafees" , 7546039528 , c)               # employee object creatd
#
# e.empinfo()
#===============================================
#
# class x:
#
#     a =10
#     def __init__(self):
#         self.b = 20
#
#     def m1(self):
#         print("m1 method of x class")
#
# class y:
#     c = 30
#     def __init__(self):
#         self.d = 40
#
#     def m2(self):
#         print("m2 method of y class")
#
#     def m3(self):
#         x1 = x()                 # object created of  class  x
#         print(x1.a)
#         print(x1.b)
#         x1.m1()
#
#         print(y.c)         # accessing static variable by using class name
#         print(self.d)
#         self.m2()                   # m2 method calling
#         print("m3 method of y class")
#
# y1 = y()            # object created
# y1.m3()             #  m3 method calling
#------------------------------------------------------------



"""Inheritance  (is-A-Relationship)"""

# whatever  variable , method and constructor aavailaible in the parent class
# by default available to the child class and we are not required to rewrite




"""what ever member present in parent class are by default available to the child class through inheritance"""
#
# class p:               #  parent class
#
#     def m1(self):
#         print("parent class method")
#
# class c(p):         # child class
#
#     def m2(self):
#         print("child class method")
#
# c = c()
# c.m1()             # parent class method calling    by using child class object
# c.m2()             # child class method calling
# -----------------------------------------------
#
# class p:             # parent class
#     a = 10
#     def __init__(self):
#         self.b = 20
#
#     def m1(self):
#         print("present instance variable ")
#
#     @classmethod
#     def m3(cls):
#         print("present class method")
#
#     @staticmethod
#     def m2():
#         print("present static method")
#
# class c(p):            # child class
#     pass
#
# c = c()                 # object created
# print(c.a)
# print(c.b)
# c.m1()
# c.m2()
# c.m3()
#------------------------------
#
# class p:
#     a = 10
#     def __init__(self):
#         self.b = 20
#
# class c(p):
#     c= 30
#     def __init__(self):
#         super().__init__()  # to call parents class member from child class and perform initilization activity
#         self.d = 30
#
# c1 = c()
# print(c1.a, c1.b , c1.c , c1.d)
#***
#
# class person:
#     def __init__(self , name , age):
#         self.name = name
#         self.age = age
#
#     def eatndrink(self):
#         print("eat bear and drink beer")
#
# class employee(person):
#     def __init__(self , name , age , eno , esal):
#         super().__init__(name , age)
#                      # to call parents class member from child class and perform initilization activity
#
#         self.eno = eno
#         self.esal = esal
#
#     def work(self):
#         print("coding python is very easy just like gaming")
#
#     def empinfo(self):
#         print("Employee age : ", self.name)
#         print("Employee Age : ", self.age)
#         print("employee number : ", self.eno)
#         print("employee salary : ", self.esal)
#
# e = employee("nafees" , 23 , 56255 , 43000)
# e.eatndrink()
# e.work()
# e.empinfo()

#*******************

"""IS-A  vs HAS-A  Relationship"""
# if we want to extend existing functionality with some extra functionality then we should go for Is-A Relationship
# if we don't want to extend and just we have to use existing functionality then we should go for Has-A relationship

# class car:
#     def __init__(self , name , model , color):
#         self.name = name
#         self.model = model
#         self.color = color
#
#     def getinfo(self):
#         print("car name: {} \nmodel: {} \ncolor: {}".format(self.name , self.model , self.color))
#
# class person:
#     def __init__(self, name, age ):
#         self.name = name
#         self.age = age
#
#     def eatanddrink(self):
#         print("Eat Briyani and Beer")
#
# class Employee(person):
#
#     def __init__(self, name , age , eno, esal , car):
#         super().__init__(name , age)
#         self.eno= eno
#         self.esal = esal
#         self.car = car
#
#     def work(self):
#         print("coding python is very easy just like drinking chilled beer")
#     def empinfo(self):
#         print("Employee Name: ", self.name)
#         print("Employee age: ", self.age)
#         print("Employee Number: ", self.eno)
#         print("Employee salary: ", self.esal)
#         print("\nEmployee CarInfo:: ",self.car)           # accessing car object
#         self.car.getinfo()                                # calling car class instance method, (Has-a-Relation)-
#
# c= car("innova", "2.5v", "Grey")                          #car object created
# e= Employee("nafees", 24, 7546039, 45000, c)              # employee object created
# e.eatanddrink()
# e.work()
# e.empinfo()

"""Composition and Aggregation"""
#Composition :-
# without existing container object if there is no chance of existing contained object
# then the container and contained object are strongly associated and strong association is nothing but composition

#Aggregation :-
# wihtout existing container object if there is a chance of contained object then the container and contained object
# are weakly associated and that weak association is nothing but Aggregation


"""Coding example"""
#
# class student:
#     collegeName = "nafees_class"
#
#     def __init__(self, name):
#         self.name = name
#
# print('college_name: ', student.collegeName)                 # Aggregation
# s = student('nafees')
# print('student_name: ', s.name)                              # composition

#------------------------------------
"""Conclusion"""

# class p:
#     def __init__(self):
#         print("Address of self: ", id(self))
#
# class c(p):
#     pass
#
# c= c()
# print("Address of c object: ", id(c))
#------------------------------------

class person:
    def __init__(self, name  ,  age ):
        self.name = name
        self.age = age

class student(person):
    def __init__(self , name, age, rollno, marks):
        super().__init__(name , age)
        self.rollno = rollno
        self.marks = marks

    def __str__(self):
        return 'Name= {} \nAge= {} \nRollno= {} \nMarks= {}'.format(self.name, self.age, self.rollno, self.marks)

s1 = student("nafees" , 24 , 39, 90)         # child class object created and both child and parents class constructor called automatically

print(s1)






































































