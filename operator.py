# OPERATORS
#=================
"""
1. Arithematic Operator
2. Relation operator
3. Logical Operator
4. Bitwise operator
5. Assignment opeartor
6. Special operator

"""
"""
# Arithematic Operator
1. +
2. -
3. * 
4. /   division operator
5. %  module operator
6. //  floor division operator
7. **  power operator , exponent operator

"""

# a=10.5
# b=2
#
# print("a+b = ", a+b)
# print("a-b = ", a-b)
# print("a*b = ", a*b)
# print("a/b = ", a/b)
# print("a//b = ", a//b)
# print("a%b = ", a%b)
# print("a**b = ", a**b)

#print("nafees"+ 10)      # error

# print("nafees"+ "10")
#
# print(2 * "nafees")

# print("nafees" + "nafees")
"""
2. Relation operator
"""
# a = 10
# b = 20
#
# print("a>b", a>b)
# print("a>=b", a>=b)
# print("a<b", a<b)
# print("a<=b" , a<=b)
#
# print()
# s1=  "nafees"
# s2=  "nhm"
#
# print("s1>s2: ", s1>s2)
# print("s1<s2: ", s1<s2)
# print("s1<=s2: ", s1<=s2)
# print("s1>=s2: ", s1>=s2)
#
# print(ord('n'))
# print(ord('a'))
#
#
# print(True > False)
# print(True < False)
# print(True > False)
# print(False >= True)
#
# print(10 > False)
# print("10" > "gaurav")
# print(ord('g'))
# print(chr(65))

#============================

# a = 10
# b= 20
#
# if (a>b):
#     print("a is greater")
#
# else:
#     print("b is greater")
#===============================
#
# """3. Logical Operator"""        # 0 means  False   and   non zero means True
# print("logical operator")
# #and                   return True if both argument is True
# print(True and True)
# print(False and False)
# print(False and True)
# print(True and False)
#
# print(10 and 0)
# print(0 and 20)
# print("nafees" and "ahm")
# print(" "  and " ")          # empty string treated as False
# print(" " and "abcd")
#
#
# #or                     return True if atleast one argument is True
# print(True or True)
# print(False or False)
# print(False or True)
# print(True or False)
#
# print(10 or 20)
# print(0 or 20)
# print("nafees" or "ahm")
# print([ ]  or "nafees")          # empty string treated as False
# print(" " or "abcd")
#
#
# #not                    Complement
# print(not True)
# print(not False)
#                                    # the result always in boolean
# print( not "nafees")
# print(not " ")
# print(not 0)
# print(not 1)


# write  a program to create valid username and password

# username= input("enter username: ")
# paswd= input("Enter password: ")
#
# if username=="nafees" and paswd=="ahm":
#                 print(":::Valid User:::")
#
# else:
#                 print(":::Invalid User:::")

#=================================================

"""
Bitwise Opeartor
&  --->  Bitwise and
| ---->  Bitwise or
^ --->   Bitwise x-or
~  -->   Bitwise complement operator
<< --->  Left shift operator
>>  -->  Right shift operator
"""
"""
print(True & True)         # only  accepted int   and bool   arg

print(4 & 5)      #  4
print(1 & 2)    #  0

print( 4 |  5)     #  5

print(4 ^ 5)
"""

"""
# left shift 
print( 10 << 2)    # 40

# right shift
print( 10 >> 2 )    #    2


print((True    <<    2))     #  4
print(True  >>  2)           # 0

print( True  >> True)
"""
#=========================================

#    Assignment operator
"""
 +=
 -=
 *=
 /=
 %=
 //=
 **=
 &=
 |=
 ^=
 <<=
 >>=
"""
#
# x= 10
# x/=5          #  x= x % 5
# print(x)
#
# a= 10
# a**=2          #  a= a**2
# print(a)
#

# a=  10
# b=  20
#
# c =  30  if a>b  else 40
#
#
# print(c)in


# a =  int(input("enter  1st number: "))
# b= int(input("enter 2nd no: "))
#
# min=  a  if a<b   else b
#
# print("minimum number: ",min)
#=============================================


# special operator
"""1. identity operator"""    #  is   ,  is not
#
# a= 10
# b= 10
#
# print(a is b)
# print( a is not b)
#
# print(a==b)
#

"""2. Membership operator"""    #   in  ,  not in

l= "nafees"

print("n" in l)    # True

print("s" not in l)    #  False

print("d" in l)     #  False































