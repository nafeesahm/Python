
"""Tuple"""

# t = (10,20,30,40)
# print(t)
# print(type(t))
#
#
# t = (10,)
# print(type(t))
# print(t)

""""by using tuple() function
"""
#
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
t = (10 ,20  ,30 ,40 ,50)
print(t[0])         # 10
print(t[-1])        #  50
print(t[100])       #  IndexError: tuple index out of range

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












