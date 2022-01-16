# List Data Type


# l = " learning python is very easy"
# print(l)
# print(type(l))
#
# s= l.split()
# print(s)
#
# print(s[1])
# print(type(s))

# s= list(range(0, 10, 1))
# print(s)
#
# a= list(range(0, 10, 2))
# print(a)


# list= [10,20,30,40,5]
# print(list[0])
# print(list[-1])
# print(list[10])
#========================

# n = [1,2,3,4,5,6,7,8,9,10,11]

# print(n[2:4])
#
# print(n[4:100])
#=============================

# n = [0,1,2,3,4,5,6,8,7,9]
#
#
# for x in n:
#     if  x%2== 0:
#         print(x)


# n= "nafees"
#
# a= len(n)
#
# print(a)
#===============================

# n = [100,111,222,333,444,555,666,888,77,99]
#
# print(n.index(222))

#============================

# n = [1,"a",2,3,"a",5,666,"b","a",99]
#
#
# print(n.count("a"))
# print(n.count(111))
#==============================

# n = [1,"a",2,3,"a",5,666,"b","a",99]
#
# n.insert(13, 888888)
# print(n)
#
# print(n.index(888888))
#===================================

# extend()

# order1= ["chicken", "mutton", "fish"]
# order2= ["egg", "RC", "FO"]
#
# print(order1)
# print(order2)
#
# order1.extend(order2)
# print(order1)
#================================
# order1= ["chicken", "mutton", "fish"]
# order2= ["egg", "RC", "FO"]
# order3= ["1", "2", "3"]
#
# order1.extend(order2)
# print(order1)
# a= order1
#
# print(a)
#
# a.extend(order3)
# print(order1)
#=========================

# order1= ["chicken", "mutton", "fish","nafees"]
# print(order1.pop(3))
#
# print(order1)
#============================

# order1= [11,2,3,422,4,56,7,54,64,3,89,9]
# order1.sort()
#
# print(order1.index(3))
# print(order1)
#===========================

# order1= [11,2,3,422,4,56,7,54,64,3,89,9]
# print(order1)
# print("after clear")
# order1.clear()
# print(order1)
#=======================


x= [10 , 20 , 30 , 50, 70]
print(x)
print(id(x))
y = x.copy()
print(id(y))
print(y)
y[1]= 777
print(y)
print(id(y))