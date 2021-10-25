"""type of variable
1. Global Variable: * The variables which are declared outside the function are called global variables
                    * These variables can be accessed in all function of that modules

a= 10
def f1():
      print(a)
def f2():
      print(a)
f1()
f2()
--------------------------------------"""
#global variable

# a=10        #global variable
#
# def f1():
#     global a
#     a=777
#     print(a)
#
# def f2():
#     print(a)
#
# f1()
# f2()
#-----------------------------

# a=10
# def f1():
#     a=777
#     print(a)      #first priority a=777  local variable
#     print(globals()['a'])     # or  print(globals().get('a'))  o/p=10     // globals() like a dictionary{}
#
# f1()

"""--------------------------------------
2. Local Variables: * The Local variables which are declared inside a function are called local variables
                    * Local variables are availables only for the function in which we decided it.  
                         i.e, from outside of function we can't accessed 

def f1():
      a=10     #LOCAL VARIABLE
      print(a)

def f2():

      print(a)    # we can't use local variable a=10
f1()
f2()       #  ERROR
# ------------------------------------"""

def factorial(n):
            if n==0:
                result= 1
 
            else:
                result= n * factorial(n-1)
a= factorial(4)
print("factorial of is : ", a)


