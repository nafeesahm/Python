# type of method
"""
1. instance method
2. class method
3. static method
"""
"""instance method"""

# class student:
#     def __init__(self, name, marks):
#         self.name= name
#         self.marks= marks
#
#     def display(self):
#         print("Hii .. ", self.name)
#         print("your marks is.. ", self.marks)
#
#     def grade(self):
#         if self.marks >= 60 and self.marks <= 100:
#             print("you got first position")
#
#         elif self.marks >= 50 and self.marks < 60:
#             print("you got second position")
#
#         elif self.marks >= 30 and self.marks < 50:
#             print("you got third position")
#
#         elif self.marks <= 30:
#             print("you are failed")
#         else:
#             print("invalid data")
# n= int(input("Enter number of student : "))
# for x in range(n):
#              name= input("Enter name: ")
#              marks= int(input("Enter marks: "))
#
#              s= student(name, marks)
#              s.display()
#              s.grade()
#              print()
#---------------------------------------------------------------------

# setter and getter method

# class student:
#     def setname(self, name):
#         self.name= name
#
#     def getname(self):
#         return self.name
#
#
#     def setmarks(self, marks):
#         self.marks= marks
#
#     def getmarks(self):
#         return self.marks
#
# n= int(input("Enter number of student : "))
# for i in range(n):
#              s= student()
#              name= input("Enter name: ")
#              s.setname(name)
#
#              marks= int(input("Enter marks: "))
#              s.setmarks(marks)
#
#              print("Hiii...", s.getname())
#              print("your marks is..", s.getmarks())
#              print()
#######################################################################################

"""class method"""

# class bird:
#     wing= 2
#     @classmethod
#     def fly(cls, name):
#         print("{}  fly with {} wings.." .format(name, cls.wing))
#
# bird.fly("parrot")
# bird.fly("crow")
#----------------------------------------
#
# class animal:
#     legs= 4
#     @classmethod
#     def walk(cls, name):
#         print("{}  walk with {} legs..." .format(name, cls.legs))
#
# animal.walk("dog")
# animal.walk("cat")

#---------------------------------------------------------------

# program to track the number of object created for a class
#
# class test:
#
#     count= 0
#     def __init__(self):
#          test.count= test.count + 1
#
#     @classmethod
#     def no_of_object(cls):
#         print("The number of object created for a test class..: ", cls.count)
#
# test.no_of_object()
#
# t= test()                  # object created
# test.no_of_object()
# t1= test()                  # object created
# t2= test()                  # object created
# t3= test()
# test.no_of_object()
############################################################################
"""static method"""
#
# class nafeesmath:
#     @staticmethod
#     def add(x,y):
#         print("The sum : ", x+y)
#
#     @staticmethod
#     def product(x,y):
#         print("The product : ", x*y)
#
#     @staticmethod
#     def average(x,y):
#         print("The average : ", (x+y)/2)
#
# nafeesmath.add(10,30)
# nafeesmath.product(10,30)
# nafeesmath.average(10, 30)
#---------------------------------------------------

"""passing member of one  class to another class"""

class Employee:
    def __init__(self, eno, ename, esal):
        self.eno= eno
        self.ename= ename                  # instance variable
        self.esal= esal

    def display(self):                     # instance method
        print("Employee number: " , self.eno)
        print("Employee name: ", self.ename)
        print("Employee salary: ", self.esal)


class test:
    def modify(emp):                            # instance method
        emp.esal= emp.esal + 20000             # instance variable

        emp.display()


e= Employee(100, "nafees", 10000)               # object created employee class

test.modify(e)




































