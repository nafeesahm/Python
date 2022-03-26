# #self   variable:
#
# class student:
#     def __init__(self):            # self is a reference variable, which is pointing to the current object
#
#             print("address of self inside class", id(self))
#
# s = student()              #both self and s refrence variable have same address (one obj two ref var)"""
#
# print("address of self outside of the class: ", id(s))
#
#=========================================

# class test:
#     def __init__(self):
#         print("Constructor")
#
#     def m1(self, x):
#         print("x value is : ", x)
#
# t= test()
#
# t.m1(10)
#============================

class student:

    def __init__(self, name, roll, marks):
        self.name= name
        self.roll= roll
        self.marks= marks

    def talk(self):
        print("Hello my name is : ", self.name)
        print("my roll number is: ", self.roll)
        print("my marks is : ", self.marks)

s= student("nafees", 39, 90)

s.talk()






















