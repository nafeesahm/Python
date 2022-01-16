
"""Tuple"""

# t = (10,20,30,40)
# print(t)
# print(type(t))


# t = (10,)
# print(type(t))
# print(t)

""""by using tuple() function
"""

# list  =  [10 , 20 ,30]
# t = tuple(list)
# print(t)
#
# t = tuple(range(10 ,20 , 2))
# print(t)

# t = tuple("nafees")
# print(t)


"""accessing element  of tuple:   by using index
"""
# t = (10 ,20  ,30 ,40 ,50)
# print(t[0])         # 10
# print(t[-1])        #  50
# print(t[100])       #  IndexError: tuple index out of range

#
#
# t = (10 ,20  ,30 ,40 ,50)
#
# for x in t:
#     res = x*3
#     print(res, end = ' ')


"""important function of tuple"""

# t = (10, 90, 30, 70, 5 , 60)
# print(sorted(t))
# print(min(t))          #5
# print(max(t))          #90


# t1 = (10, 20, 30)
# t2 = (40, 50 , 60)
# t3 = (10, 20 , 30)
#
# print(cmp(t1 , t2))        # -1
# print(cmp(t1 , t3))        #  0
# print(cmp(t2 , t3))        # +1
                                                    # NameError: name 'cmp' is not defined
""" cmp() function  is  available   only   in  python 2 , but not in python3 
"""
#
# t = (10,20,30,40,5)
# t1 = (33 , 88 , 9 ,7)
# t4 = t+t1
# print(t4)


#
# # index()
# t= (10 ,20 , 30 ,20)
# print(t.index(10))
# print(t.index(30))
# print(t.index(20))
#----------------------------------------------------

# packing and unpacking
# a = 10
# b = 20
# c = 30
# d = 40
# t = a,b,c,d
# print(type(t))
# print(t)
"""---------------------"""
#
# t =  (x**2 for x  in range(1,6))            # 1,2,3,4,5
# print(type(t))                   #   here  we are  not getting tuple object and we are getting generator object
# for x in t:
#      print(x)


"""write  a program  to take of Number form the keybord and print   its sum and average"""

# t = eval(input("Enter tuple of Number : "))      # (10,20,30,40)
#
# sum = 0
# for x in t:
#     sum = sum + x
# print("The sum: " ,sum)
#
# print("The Average : ", sum/len(t))

#
#
# t1 = (10 ,'nafees ' , True , 3.5)
# print(t1)
# print(type(t1))
#




















