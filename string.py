# # String Data Type    : any sequence of charecter
# #
# # s= """nafees '
# #       ahmad
# #       ben
# #
# #        """
# # print(s)
# #
# #============================
#
# """ String Data Type    : any sequence of charecter"""
# #
# # s = "this is \" symbol"
# #
# # print(s)
# #
# #
# # n = "nafees"
# #
# # i= n[2]
# # print(i)
# #
# #
# #
# # s= "varsha gupta"
# # print(s[-1])
# #
# # print(s[10])
#
#
# #
# # s=  input("Enter some string: ")     # gaurav
# #
# # i = 0
# # for x in s:
# #
# #     print(f"The character present at positive index {i} and at negative index {i-len(s)} is  : {x}")
# #
# #     i = i + 1
#
#
# # accessing character by using slice operator
# """
# syntax:
# s[startindex : endindex :  step]     , step - increment value
#                 end - 1
#
# """
# #
# # s= "abcdefghijk"
# # a= s[2:7]
# # print(a)
# #
# # print(s[2:])
# # print(s[:])
# # print(s[:7])     # abcdefg
# # print(s[0:10])
# # print(s[-1:: 1])
# #----------------------------------------
#
# # write a programe to access each character of string in forward and backward by using while loop
#
#
#
# #
# # s = "LEARNING PYTHON IS VERY EASY"
# # n = len(s)
# # i =  0
# # print("Forward drection : ")
# # while i<n:
# #     print(s[i] , end = '')
# #     i = i+1
# #
# # print("\nBackward direction:  ")
# # i = -1
# # while i>=-n:
# #     print(s[i] , end = '')
# #     i = i-1
# # ---------------------------------
# #
# # s = input("Enter some string : ")    # gaurav
# # subs = input("Enter sub string : ")
# # if subs in s:
# #     print(subs , "is found in main sring")
# #
# # else:
# #     print(subs, "is not found in main string")
# #----------------------------------
#
# """removing space from the string"""
#
# # 1 . rstrip     - >    to remove spaces at right hand side
# # 2 . lstrip     - >     to remove spaces from left hand side
# # 3 . strip      - >     to remove spaces  from both side
# #
# # city  = input("Enter city name : ")
# # stp = city.strip()
# # if stp == 'hyderabad':
# #     print("HELLO Hyderabad ... adab")
# #
# # elif stp=='chennai':
# #     print("hello madrasi... vanakkam")
# #
# # elif stp == 'banglore':
# #     print("hello kannadiga... shubhodaya")
# # else:
# #     print("your interd city is invalid")
# #----------------------------------------
#
# # finding substring
# """we can use 4 for method"""
#
# #for Forward direction
# """ 1. find()
#     2. index()
# """
# # for Backward direction
# """ 3. rfind()
#     4. rindex()
# """
#
# """Find() and  index()"""
# #
# # s = "LEARNING PYTHON IS VERY EASY"
# # print(s.find('PYTHON'))    # 9
# #
# # print(s)
# # #print(s.index('guru'))
# # print("length  = ", len(s))
# #
# # print(s.find('A'))
# # print(s.find('A',15, 29))
#
#
#
# #
# # s =  input("Enter main string : ")    # nafees ahmad
# # subs  =  input("Enter sub string : ")
# #
# # try:
# #     n = s.index(subs)
# #     print("index number is : ", n)
# #
# # except ValueError:
# #     print(":::substring not found:::")
# #
# # else:
# #     print("Substring Found")    #  20,,. 1
# #***********
#
# """program to display all position of substring in a given main sring"""
#
# # s = input("Enter main string : ")
# # subs = input("enter sub string: ")
# #
# # Flag = False
# # pos = -1
# # n = len(s)
# # while True:
# #     pos = s.find(subs, pos+1 , n)
# #     if pos==-1:
# #         break
# #
# #     print("Found at index : ", pos)
# #     flag = True
# # if flag==False:
# #     print("Not Found")
# #--------------------
#
# """Repalce"""
# # s = "Learning  python is very easy"
# # s1 = s.replace('easy', 'difficult')
# # print(s1)
# # print()
# # s2 = s.replace('is', '       ')
# # print(s2)
#
#
# # s = "A B C"
# #
# # print(s)
# # n= []     # ['A' , 'B' , 'C']
# # for x in s:
# #     if x=='A':
# #         n.append(x)
# #
# #     elif x=='B':
# #         n.append(x)
# #
# #     elif x=='C':
# #         n.append(x)
# #
# # print(n)
# #
# # list= ''.join(n)
# # print(list)
# #*************************
#
#
#  counting substring in the given string
#
# """we can find the number of occurances if substring present in given string """
# # count()
#
# s = "abababacabacabac"
# print(s.count('a'))
#
# print(s.count('ab'))
# print(s.count('a' , 3,7))
#**************************

# changing case of string

"""
1. upper()  => to convert all character to upper case
2. lower()  => to convert all character to lower case
3. swapcase() => to convert all lower case  character into upper and all upper case into lower case
4. title()  =>  to convert  all character to title case , first character in every word should be upper case and
                           and all remaining  character should  be lower case
5. capitalize() =>   only first character  will be converted to upper case  all remaining  character
                       can be  coverted  lower
"""
# s = "Learning Python is Very easY"
# print(s.upper())
# print(s.lower())
# print(s.capitalize())
# print(s.title())
# print(s.swapcase())

#********************
"""checking starting and Ending part of the string """
#
# s = "versha gupta  abc iit nit"
# print(s.startswith('versha'))
#
# print(s.startswith('iit'))
#
# print(s.endswith('nit'))
# print(s.endswith('gupta'))
#******************

"""to check type of character present in string """
"""
1. isallnum()
2. isalpha()
3. isdigit()     or isdecimal()
4. islower()
5. isupper()
6. isspace()
7  isspace()
"""
#
# s = input("Enter any character: ")
# if s.isalnum():
#     print("Alpha numeric character")
#
#     if s.isalpha():
#         print("Alphabet character")
#
#         if s.islower():
#             print("Lower case alphabet character")
#
#         else:
#             print("Upper case  alphabet character")
#
#     else:
#         print('it is digit')
#
# elif s.isspace():
#     print("it is a space character")
#
# else:
#     print("non space special character")
#***********************************
"""Formated string"""
# we can formate the string with variable  bu using replacement {} and .format() method
#
# name = 'nafees'
# salary =  33000
# age = 23
# print("{}'s salary is  {} and his age is  {} ".format(name,salary,age ))



# write a programs to reverse  the string
"""1st way"""
# s = "it may be rain today"
# print(s)
# print(''.join(reversed(s)))

"""2nd way"""
# print(s[::-1])

"""3rd way"""
# s = input("enter some string : ")
# i = len(s) - 1
# target = ""
# while i>=0:
#     target = target  + s[i]
#     i = i - 1
#
# print(target)

"write a program to reverse order of words"
#
# s1="python is a language"
# s2=s1.split()
# print(s1)
# print(s2)
# s3=(reversed(s2))
# print(' '.join(s3))

# =======================================================
#========================================================

