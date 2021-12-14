"""Control Flow""" # flow control describe the order in which statement  will be executed at runtime
#----------------------
"""1. conditional or selecttive statement - if , if-else , if-elif-else
   2. Tranfer statement  -                  break , continue ,  pass
   3. iterative statment  -                 for loop    , while  loop
"""

# if- else
#
# name = input("Enter your name : ")
# if name == "nafees":
#     print("Hello nafees good evening")
# else:
#     print("you are good boy")
#
#
# print(":::how are you:::")
#
#

"""if-elif-else"""
#
# brand  = input("Enter your fav brand: ")
#
# if brand.upper() == "RC":
#     print("it is children brand")
#
# elif brand.upper() == "KF":
#     print("it is not that much kick")
#
# elif brand.upper() == "FO":
#     print("Buy one get one free")
#
# else:
#     print("other brand are not recomemded")
#


# write a program to find biggest number from three number
#
# n1= int(input("enter 1st number : "))     # 10
# n2= int(input("enter 2st number : "))     # 20
# n3= int(input("enter 3st number : "))     # 30
#
# if n1 > n2 and n1>n3:     # 0  False                0 and 0  = 0
#     print("Biggest number is- ", n1)
#
# elif n2 > n3:      # 0 False
#     print("biggest number is - ", n2)
#
# else:
#     print("biggest number is - ", n3)

#
# n = int(input("enter number: "))
# if n%2==0:
#     print("your number is :::EVEN:::")
#
# else:
#     print("your number is :::ODD:::")

#
# k = int(input("enter range : "))
# list= []
#
# for x in range(k):
#     n = eval(input("enter value  :"))
#
#     list.append(n)
#
# print(list)




""" program to take Digit from keyboad and print value in english word """
#
# word_upto_19 = [ " ", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
#          "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
#
# word_for_tens = [" ", " ", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
#
# n = int(input("Enter a digit from 0 to 99 : "))
#
# if n == 0:
#     output= "zero"
#
# elif n<=19:
#     output= word_upto_19[n]
# elif n<=99:
#     output= word_for_tens[n//10] + " " + word_upto_19[n%10]
# else:
#     output = "please enter a value from 0 to 99"
#
# print(output)

"""Iterative statement"""

""" if we want to execute a group of statement multiple times ...
1. for loop
2. while loop

:::syntax:::
for  x  in sequence: 
         body
         activity

"""
#
# s= "nafees ahmad"
# for x in s:
#     print(x, end = "")
#

# to print character in string index wise

# s = input("enter some string: ")
# i= 0
# for  x in s:
#     print("the character present at ", i , "index is : ", x )
#     i = i+1


# to print hello 10 time
#
# for x in range(10):    # 0   to 9
#     print("Hello")
#
# for  x in range(11):
#     print(x)
#

# to display odd number  from 0 to 20
#
# for x in range(21):
#     if x%2 != 0:
#         print(x)

# to display the number  from 10 to 1 in decending order
#
# for x in range(10, 0, -1 ):
#     print(x)
#


#to display the number  from 10 to 1 in decending order
# i = 10
# for x in range(10):
#     print(i-x)
#


# to print sum of number present inside list
#
# list = [10 , 20 ,50 ,100]
#
# sum = 0
# for x in list:
#     sum = sum + x
#
# print("the sum: ", sum)

#
# list = eval(input("enter list: "))
#
# a = sum(list)
# print("The sum : ", a)


# to print number from 1 to 20 which is divisible by 3
#
# for x in range (1,21):
#         if x%3 == 0:
#              print(x)

"""While loop"""

"""
if we want to execute a group of stattement itreatively  until some condition  False ,  
then we should go for  while loop

"""

# to print number from  1 to 10 by using while loop

# x= 1
# while  x<=10:
#     print(x)
#
#     x= x+1

# to display the sum of first nth number
#
# n = int(input("Enter number: "))     # 5
#
# sum= 0
# i= 0
# while i<=n:
#     print(i, " + " , end= '')
#     sum = sum+i
#
#     i = i + 1
# print("\n The sum of frst n number : ", sum)




#
# name= " "
#
# while name!= "nafees":
#
#     name = input("Enter your name : ")
#
#
# print("Thanks for conformation")
#


"""find the number whose sum is equal to 30"""
#
# print("find the number whose sum is equal to 30")
# print()
# print(" [] + [] + [] = 30")
# print("Option : 1, 3, 5, 7, 9, 11, 13, 15 ")
#
# list = []
# for x in range(3):
#             n = int(input(f"Enter {x+1} number: "))
#             list.append(n)
#
# sum = 0
# for i in list:
#     sum = sum+i
#
# print("Sum = ", sum)
#
# if sum==30:
#     print(":::You Win:::")
# else:
#     print("you loose")
#


"""infinite loop"""
#
# i = 0
# while i<=10:
#     print("Hello_ gaurav")
#     i = i+1
#


# Nested Loop
"""loop inside anathor loop"""
#
# for i in range(3):
#     for j in range(2):                # 0, 1
#         print(f"i= {i}, j = {j}")
#         break

# for i in range(10):
#     if i%2==0:
#         continue
#
#     print(i)
#
# cart = [10 ,20 ,600 ,30 ,700 , 80 ,90]
#
# for item in cart:
#     if item>500:
#         print("insurance must be required, just skipping item ", item)
#
#         continue
#
#     print("Processing item: ", item)
#
#




# pass statement

"""
pass os a keyword in python

-> it is an empty statement
-> it is null statement
-> it won't do anything

"""
# if True:
#         pass           # pass Statement act as  place holder for future implementation
#


# def f1():
#     pass

#
# class A:
#     def __init__(self):
#         pass
#
#
# class B:
#     pass
#
#
# class C:
#     pass
#
#
# aaa = A()
#
#
# x = int(input("Enetr marks: "))
#
# if x>=35:
#     print("success")
#
# else:
#     pass



# del   >>>> delete the variable
#
# x = 10
#
# del x
#
# print(x)
#
#


# s1 = "nafees"
# s2 = s1       #  nafees
# s3 = s2       # nafees
#
# del s1         #   s1  deleted
#
# print(s2)      # nafees
# print(s3)      # nafees
#
# del s2, s3

#
# s = "nafees"
#
# s = None
#
# print(s)





"""program to generate first n prime number"""
#
# n = int(input("Enter nth value: "))         # 10
#
# count = 0
# n1 = 2             # prime number
# while True:
#     is_prime = True
#     for i in range(2  , n1//2+1):
#
#         if n1%i==0:
#             is_prime = False
#             break
#
#     if is_prime == True:
#         print(n1)
#         count = count + 1
#
#     if count == n:
#         break
#
#     n1 = n1+1


""" wap to check whether the given number is prime or not """

a= int(input("enter your number: "))

if a<= 1:
    print("it is not prime")

else:
    prime = True

    for i in range(2,a):
        if a%i == 0:
                prime = False
                break

    if prime == True:
        print("it is prime number")
    else:
        print("it is not prime")

















