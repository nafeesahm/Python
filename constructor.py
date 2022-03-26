# # program ro dimonistrate constructor will be executed only once per object
#
# class test:
#     def __init__(self):
#         print("constrctor executed")
#
#     def m1(self):
#         print("method executed ")
#
# t1= test()
# t2= test()
# t3= test()
# t1.m1()
#
#==========================================

# class student:
#     def __init__(self, name, rollno, marks):
#
#         print(":::you are inside constructor:::")
#         print("cresting instance variable and performing initilization")
#
#         self.name= name
#         self.rollno= rollno
#         self.marks= marks
#
#     def display(self):
#         print(":::you are inside method:::")
#
#         print(f"student Name: {self.name}\nstudent_rollno: {self.rollno},\nstudent marks: {self.marks}" )
#


# s1= student("nafees",39, 95)             # object created
# print("Name: ",s1.name,"\nrollno", s1.rollno,"\nMarks: ",s1.marks)
#
# print()
#
# s2= student("musfik", 22, 99)              # object created
# s2.display()                               # display method calling
#============================================================================

class test:

    def __init__(self):
        print("contructor executed")

t= test()                 # object created   and constructor  called automatically

t.__init__()             # constructor called just like a normal method
t.__init__()
t.__init__()














