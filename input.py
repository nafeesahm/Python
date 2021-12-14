# a= input("enter your no- ")
#
# print(a)
#
# print(type(a))
#

#=====================================
#
# x= eval(input("Enter number: "))
# y= eval(input("Enter number: "))
#
# z= x * y
#
# print("sum is : ", z)
#
# print(type(z))
#=======================================
#
# eno = int(input("Enter employee number: "))
# ename= input("Enter employee name: ")
# esal= eval(input("Enter Employee salary: "))
# eddrs= input("enter Employee address: ")
# married= bool(input("Employee Married? [True | [False] :: "))
#
# print()
#
# print(":::Employee confirm information:::")
#
# print("Empolyee no: ", eno)
# print("Employee Name: ",ename)
# print("Employee salary: ",esal)
# print("Employee address: ", eddrs)
# print("Employe Married ?  : ", married)

#=================================================================

"""How to read multiple value from the keyboard in single line"""
#
# a, b= [int(x) for x in input("enter 2 number: ").split()]
#
# print("product is : ", a*b)

#---------------------------------------------

# x = eval(input("enter expression: "))
# print(x)
# print(type(x))
#------------------------------------------

# a,b,c =  10 ,20 , 30
#
# print("the value is : ", a,b,c)
#
# print(a, b, c  , sep= '.')
# print(a, b, c , sep = ":")
# print(a,b,c , sep = 'gaurav')
#_------------------------------------

# end attribute
#
# print("Hello")
# print("versha_gupta")
# print("you are in the class")
#
# print()
#
# print("Hello" , end = '...')
# print("versha_gupta" , end = '__')
# print("you are in the class")
#
#
# s= "nafees"
# a= "06"
# s1= "python"
# s2= "machine_Learning"
#
# print("Hello... ", s , "you age  is : ", a , "year")
# print("you are teaching : ", s1, "and", s2)


""" Formatted string

1.   %i  -  int
2.   %d  -  int
3.   %f  -  float 
4.   %s  -  string type

syntax -  print("fromated string: " % (variable (list))

"""
a = 10
b = 20
c = 30

print("a value is  %i" %a)

print("b value is %s  and c value is %i" %(b, c))

print(f" your a value is {a}")

print("your a value {} b value is {} : ".format(a,b))


























