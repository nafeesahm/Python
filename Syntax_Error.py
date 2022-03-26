"""in programming there are two type of errors are possible """
"""
1. Syntax errors
2. Runtime errors 

"""
# Syntax errors:
"""the errors which occur because of invalid syntax are called syntax errors"""
"""
x = 10
if x==10
    print("hello")              # SyntaxError: invalid syntax
"""

"""
print "Hello"          #SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Hello")?

"""

# Runtime errors :
"""
♦ also known as Exception Handling
♦ while executing the program if something goes wrong because of end user input or 
  programming logic or memory problem etc... then we will get Runtime error.
  
"""
# print(10/0)           """ZeroDivisionError: division by zero"""

# print(10/ten)         """NameError: name 'ten' is not defined"""


# x = int(input("Enter Number : "))
# print(x)
"""Enter Number : ten"""
"""ValueError: invalid literal for int() with base 10: 'ten'"""

# Exception Handling concept applicable for runtime errors , but not for syntax...

"""♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦•♦"""

"""What is Exception """
# an unwanted and unexpected event that disturbs normal flow of program is called exception.

"""
# Q. What is the purpose of Exception Handling?
It is highly recommended to handle exceptions. The main objective of exception handling 
is Graceful Termination of the program (i.e we should not block our resources and we 
should not miss anything)
"""
"""
# Q. What is the meaning of Exception Handling?
Exception handling does not mean repairing exception. We have to define alternative way 
to continue rest of the program normally.
"""


# Default Exception Handing in Python:
"""
• Every exception in Python is an object. For every exception type the corresponding 
  classes are available.
• Whenever an exception occurs PVM will create the corresponding exception object 
  and will check for handling code. If handling code is not available then Python
  interpreter terminates the program abnormally and prints corresponding exception 
  information to the console.
• The rest of the program won't be executed
"""
#
# print("hello")
# print(10 / 0)              # ZeroDivisionError: division by zero
# print("hiiii")
#

# Python's Exception Hierarchy:
"""
BaseException                  (parent class)
♦
♦
"""
#☻ Exception                # (child class)

"""1 . Attribute Error"""
"""2 . Arithmetic Error"""    # ZeroDivision Error , FloatingPoint Error  , Overflow Error
"""3 . EOF Error"""
"""4 . Name Error"""
"""5 . Lookup Error"""        # Index Error , Key Error
"""6 . OS Error"""           # FileNotFound Error , Interrupted Error , Permission Error , TimeOut Error

"""7 . Type Error"""
"""8 . Value Error"""

"""
☺ Every Exception in Python is a class. 
•  All exception classes are child classes of BaseException.i.e every exception class 
   extends BaseException either directly or indirectly. Hence BaseException acts as root 
   for Python Exception Hierarchy.
•  Most of the times being a programmer we have to concentrate Exception and its child 
   classes
"""

# ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦
# print("nafees")
# print(10/0)
# print("ahmad")
#------------

# print("its ... me ben")
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print(10/2)
# print("hey now you are good to go")

#--------------------
"""how to print exception information"""
# try:
#     print(10/0)
# except ZeroDivisionError as msg:
#     print("Exception raised and its descreption is : ", msg)
#     print("Exception raised and its descreption is : ", type(msg))
#     print("Exception raised and its descreption is : ", msg.__class__)
#     print("Exception raesed and its descreption is : ", msg.__class__.__name__)

#------------------------

"""try with multiple except block"""
# try :
#     x = int(input("Enter first number : "))
#     y = int(input("Enter second number : "))
#     print(x/y)
# except ZeroDivisionError:
#     print("can't devide with zero ")
# except ValueError:
#     print("please provide int value only")

#-----------------
#
# try:
#     x= int(input("Enter first number : "))
#     y= int(input("Enter second number : "))
#     print(x/y)
# except ArithmeticError:
#     print("Arithematic Error")         # top to bottom
#
# except ZeroDivisionError:
#     print("Zero division Error")

#-------------------
"""single except block that can handle multiple exception"""
# try :
#     x = int(input("Enter first number : "))
#     y = int(input("Enter second number : "))
#     print(x/y)
# except (ZeroDivisionError , ValueError) as msg :
#     print("plzz provide valid number only and problem is : ", msg)
#---------------

"""default except block"""
# try:
#     x = int(input("Enter first number : "))
#     y = int(input("Enter second number : "))
#     print(x/y)
# except (ZeroDivisionError):
#     print("Zero Division Error... can't divide with zero")
# except:
#     print("Default Exception ... plzz provide valid input only")

# --------------------
# try :
#     print(10/0)
# except :
#     print("Default Except")                SyntaxError: default 'except:' must be last
# except ZeroDivisionError:
#     print("zero division error")

#==================

"""Finally"""
"""
try:
   risky code
except:
    handling code 
finally:
    cleanup code
    

"""
#
# try:
#     print("try")
# except:
#     print("except")
# finally:
#     print("finally")
# ===========
# try:
#     print("try")
#     print(10/0)
# except ZeroDivisionError:
#     print("zero division error")
# finally:
#     print("finally")
# ----------------
# try:
#     print("try")
#     print(10/0)
# except ValueError:
#     print("except")
# finally:
#     print("finally")
#----------------

"""ther is only one situation where finally block won't be executed 
i.e... whenever we are using os._exit(0) function"""
#
# import os
# try:
#     print("try")
#     os._exit(0)
# except NameError:
#     print("except")
# finally:
#     print("finally")
#--------------
# try:
#     print("outer try block")
#     try:
#         print("inner try block")
#         print(10/0)
#     except ZeroDivisionError:
#         print("inner except block....zero division error")
#     finally:
#         print("inner finally block")
# except:
#     print("outer except block")
# finally:
#     print("outer finally block")
#--------------------------




"""Type of exception"""
"""
1 . Predefined Exception
2 . User define Exception
"""


# 1 ... Predefined Exception
"""alsp known as inbuilt exception
•the exception which are raised automatically by python virtual machine whenever a particular event uccurs are called
predefined exception
"""
# f = None
# try:
#     a= input("Enter File Name : ")
#     f = open(a, 'r')
#
# except:
#     print("Some problem while locating / opening file")
# else:
#     print("File opend successfully")
#     print("♦"*30)
#     print(f.read())


# 2 . User Define Exception
"""also known as customized exception or programatic exception"""
"""Sometime we have to define and raise exception explicity to indicate that something goes wrong ,
such type of exception are called user define exception
"""

"""Programmer is rsponsible to define these exception python not having any idea about these , 
hence we have to raise explicity based on our requirement 
by using "raise"  keyword
"""

class TooYoungException(Exception):
    def __init__(self , arg):
        self.msg = arg

class TooOldxception(Exception):
    def __init__(self , arg):
        self.msg = arg

age  = int(input("Enter age : "))
if age<18:
    raise TooYoungException("plzzz wait some more time you will get best match soon")
elif age>60:
    raise TooOldxception("Your age already crossed maried age ...no chance of getting married")
else:
    print("You will get match detail soon by email.!!!!")



