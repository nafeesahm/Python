"""
poly means many. Morphs means forms.
Polymorphism means 'Many Forms'.

Eg1: Yourself is best example of polymorphism.In front of Your parents You will have one
type of behaviour and with friends another type of behaviour.Same person but different
behaviours at different places,which is nothing but polymorphism.

Eg2: + operator acts as concatenation and arithmetic addition
Eg3: * operator acts as multiplication and repetition operator

Eg4: The Same method with different implementations in Parent class and child
classes.(overriding)

"""

#Overloading
"""
1) Operator Overloading
2) Method Overloading
3) Constructor Overloading
"""

#Overriding
"""
1) Method Overriding
2) Constructor Overriding
"""


"""Overloading"""
"""
We can use same operator or methods for different purposes.
Eg 1: + operator can be used for Arithmetic addition and String concatenation
print(10+20)#30
print('nafees'+'ahmad')     # nafeesahmad
 
 
Eg 2: * operator can be used for multiplication and string repetition purposes.
print(10*20)    #200
print('durga'*3)#durgadurgadurga


Eg 3: We can use deposit() method to deposit cash or cheque or dd
deposit(cash)
deposit(cheque)
deposit(dd)
 
There are 3 types of Overloading
1) Operator Overloading
2) Method Overloading
3) Constructor Overloading
"""

# 1) Operator Overloading
"""We can use the same operator for multiple purposes, which is nothing but operator 
overloading.
☻ Python supports operator overloading
"""

#Demo program to use + operator for our class objects:
# class Book:
#         def __init__(self,pages):
#                 self.pages=pages
#
# b1=Book(100)
# b2=Book(200)
# print(b1+b2)           # TypeError: unsupported operand type(s) for +: 'Book' and 'Book'

"""
We can overload + operator to work with Book objects also. i.e Python supports 
Operator Overloading.
⚽ For every operator Magic Methods are available. To overload any operator we have to 
override that Method in our class. 
⚽ Internally + operator is implemented by using __add__() method.This method is called 
magic method for + operator. We have to override this method in our class. 
"""

# Demo Program to Overload + Operator for Our Book Class Objects:
#
# class book:
#     def __init__(self, pages):
#         self.pages = pages
#         print(self.pages)
#
#     def __add__(self, other):                # self=100 , other=200    , magic method
#         total_pages = self.pages + other.pages
#         return total_pages
# b1 = book(100)
# b2 = book(200)
# print("Total_pages = ", b1+b2)

# The following is the list of operators and corresponding magic methods.
"""
1) +       object.__add__(self,other)
2) -       object.__sub__(self,other)
3) *       object.__mul__(self,other)
4) /       object.__div__(self,other)
5) //      object.__floordiv__(self,other) 
6) %       object.__mod__(self,other)
7) **      object.__pow__(self,other)
8) +=      object.__iadd__(self,other)
9) -=      object.__isub__(self,other)
10) *=     object.__imul__(self,other)
11) /=     object.__idiv__(self,other)
12) //=    object.__ifloordiv__(self,other)
13) %=     object.__imod__(self,other)
14) **=    object.__ipow__(self,other)
15) <      object.__lt__(self,other)
16) <=     object.__le__(self,other)
17) >      object.__gt__(self,other)
18) >=     object.__ge__(self,other)
19) ==     object.__eq__(self,other)
20) !=     object.__ne__(self,other)
"""


# Overloading > and <= Operators for Student Class Objects:
#
# class student:
#     def __init__(self, name , marks):
#         self.name = name
#         self.marks= marks
#
#     def __gt__(self, other):
#         total = self.marks > other.marks
#         return total
#
# s1 = student("nafees" , 100)
# s2 = student("ahmad", 200 )
# print(s1 > s2)
# print(s1 < s2)      # automatic pvm will take care to reverse this, we are not require to use __lt__(self,other)
#--------------------


# class student:
#     def __init__(self, name , marks):
#         self.name = name
#         self.marks= marks
#
#     def __le__(self, other):
#         total = self.marks <= other.marks
#         return total
#
# s1 = student("nafees" , 100)
# s2 = student("ahmad", 200 )
# print(s1 <= s2)
# print(s1 >= s2)      # automatic pvm will take care to reverse this, we are not require to use __ge__(self,other)

#
# class employee:
#     def __init__(self, name, salaryperday):
#         self.name = name
#         self.salaryperday=  salaryperday
#     def __mul__(self, other):                               # magic function
#         result = self.salaryperday * other.workingday
#         return result
#
# class timesheet:
#     def __init__(self,name, workingday):
#         self.name = name
#         self.workingday = workingday
#     def __mul__(self, other):                                  # magic function
#         return self.workingday * other.salaryperday
#
# e = employee("nafees" , 500)
# t = timesheet("nafees" , 25)
#
# print("this month salary : " , e*t)          # order is important
# print("this month salary: " , t*e)
#
#-----------------


"""important of __str__() method"""

# class student:
#     def __init__(self , name , rollno , marks):
#         self.name = name
#         self.rollno = rollno
#         self.marks = marks
#
# s1 = student('nafees' , 39 , 96)
# s2 = student('ahmad' , 33 , 77)
# print(s1)                    # whenever we trying to print obj reference internally __str__() method called
# print(s2)                    # default implementation responsible to provide output


# class student:
#     def __init__(self , name , rollno , marks):
#         self.name = name
#         self.rollno = rollno
#         self.marks = marks
#     def __str__(self):
#         #return self.name
#         return " Name : {} \n ROllno : {} \n Marks : {} \n".format(self.name , self.rollno , self.marks)
#
# s1 = student('nafees' , 39 , 96)
# s2 = student('ahmad' , 33 , 77)
# print(s1)
# print(s2)


"""overloading + opoerator for nesting requirement"""
#
# class Book:
#     def __init__(self , pages):
#         self.pages = pages
#
#     def __add__(self, other):
#         return Book(self.pages + other.pages)
#
#     def __str__(self):
#         return "The number of pages : {}".format(self.pages)
#
#     def __mul__(self, other):
#         return Book(self.pages * other.pages)
#
# b1 = Book(100)
# b2 = Book(200)
# b3 = Book(500)
# b4 = Book(600)
# print(b1+b2+b3)
# print(b1+b2)
# print(b2+b3+b4)
# print(b1+b2*b3+b4)
# print(b1*b2+b3*b4)                      # first multiply then add,  operator precedence , priority


#☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺

# 2). Method overloading

"""if 2 method having same name but different type of argument then those method are said to be overloaded method
"""
"""
☻ but in python Method overloading is not possible
♦  if we are trying to declare multuple method with same name and different number of argument 
   then python will always consider only last method
"""
"""
class test:
    def m1(self):
        print("no argument method")
    def m1(self , a):
        print("one argument method")
    def m1(self, a,b):                          # this method called
        print("two argument method")
t = test()
# t.m1()
# t.m1(10)
t.m1(30,40)
"""

# why python won't support method overloading
"""
we can not declare data type , based on provided value type will be consider automatically(dynamically type)
As type concept is not applicable ,
Method overloading concept is not applicable in python
"""
# class Test:
#     def m1(self , x):
#         #print(type(x) ,"type argument method")
#         print("{} type argument Method".format(x.__class__.__name__))
#
# t = Test()
# t.m1(10)
# t.m1(40.5)
# t.m1("nafees")

"""☻☻☻☻☻☻☻☻☻☻☻☻☻☻"""
"""How we can handle overloaded method - 2 ways :"""
# 1. Default  Argument
# 2. Variable Length Argument

"""1. Default Argument """
# class test:
#     def m1(self , a=None , b=None , c=None):
#         if a is not None and b is not None and c is not None:
#             print("3 Argument Method")
#
#         elif a is not None and b is not None:
#             print("2 Argument method")
#
#         elif a is not None:
#             print("1 Argument method")
#
#         else:
#             print("No  Argument method")
# t = test()
# t.m1()
# t.m1(10)
# t.m1(20,30)
# t.m1(30,40,50)

""""2. Variable length Argument """
# class test:
#     def m1(self , *args):
#         print("Variable length argument")
# c = test()
# c.m1()
# c.m1(10)
# c.m1(10,20)
# c.m1(10,20,30,40)
#*************

# class test:
#     def sum(self , *args):               # *args - variable length argument
#         total = 0
#         for x in args:
#             total  = total+x
#         print("sum : " ,total)
# s = test()                      # object created
# s.sum(10)
# s.sum(10,20,30)                 # sum method called
# s.sum(1,2,3,4,5,6,7,8,9)



#☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺
# 3) Constructor Overloading
"""
♦constructor overloading is not possible in python
♦if we define multiple constructor then the last constructor will be consider 
"""
"""
class Test:
    def __init__(self):
        print("NO  argument constructor ")

    def __int__(self , ):
        print("one argument constructor")

    def __init__(self, a ,b ):
        print("two argument constructor ")

# t = Test()              # Error
# t = Test(10)            # Error
t = Test(10,20)                      # object created with 2 positinal argument 
"""
"""last constructor will consider only """
"""in above program only two argument constructor is available"""
# based on  our requirement we can declare constructor with

# 1 . default argument
# 2 . variable number of argument

"""1. constructor with default argument"""

# class Test:
#     def __init__(self, a= None , b=None, c=None):
#         print("constructor with 0|1|2|3 number of arguments")
#
# t = Test()
# t1 = Test(10,20)
# t2 = Test(1,2,3)


"""2. constructor with variable number of argument"""
#
# class Test:
#     def __init__(self ,  * args):
#         print("constructor with variable number of argument ")
#
# t  = Test()
# t1 = Test(10)
# t2 = Test(10, 20)
# t3 = Test(10,20,30)
# t4 = Test(10,20,30,40,50)




#☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺

""" Overriding"""
# 1 . Method Overriding
# 2 . constructor overriding

"""overriding concept applicable for both method and constructor"""

# 1 Method overriding
"""
what ever member available in the parent class are bydefault available to the child class through inheritance
if child class not satisfied with parent class implementation then child class is allowed to redefine that method
in the child class based on it requirement. this concept is called overriding
"""
#
# class P:
#     def property(self):
#         print("flat + gold + Land")
#
#     def marry(self):
#         print("papa ki pari")
#
# class C(P):
#     def marry(self):
#         print("Katrina kaif")
#
# c= C()
# c.property()
# c.marry()
#######################
#
# class P:
#     def property(self):
#         print("flat + gold + Land")
#
#     def marry(self):
#         print("papa ki pari")
#
# class C(P):
#     def marry(self):
#         super().marry()                   # calling parent class marry method
#         print("Katrina kaif")
#
# c= C()
# c.property()
# c.marry()



# 2.  constructor overriding
"""if child class does not contain constructor then parent class constructor will be executed
"""
#
# class P:
#     def __init__(self):
#         print("parent class constructor ")
#
# class C(P):
#     pass
#
# c = C()
##################

# class P:
#     def __init__(self):
#         print("parent class constructor ")
#
# class C(P):
#     def __init__(self):
#         print("child class constructor ")
#
# c = C()
#
##################


# class P:
#     def __init__(self):
#         print("parent class constructor ")
#
#
# class C(P):
#     def __init__(self):
#         print("child class constructor ")
#         super().__init__()
#
# c = C()
######################

class p:
    def __init__(self , name , rollno, marks , id):
        self.name = name
        self.rollno = rollno
        self.marks = marks
        self.id = id

class c(p):
    def __init__(self, name , rollno, marks , id, account , password , cvv, ):
        super().__init__(name , rollno , marks , id)
        self.account = account
        self.password = password
        self.cvv = cvv

    def display(self):
        print('name : ', self.name)
        print('rollno: ', self.rollno)
        print('marks : ', self.marks)
        print('id : ', self.id)
        print('account : ', self.account)
        print('cvv : ', self.cvv)

t = c("nafees" , 39 , 97 , 66585669 , 3568540620, 220797 , 100)
t.display()















