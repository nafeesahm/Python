"""List Data Type:

If we want to represent a group of values as a single entity
where insertion order required to preserve and duplicates are allowed then we should go for list data type.

1) Insertion Order is preserved

2) Heterogeneous Objects are allowed

3) Duplicates are allowed

4) Growable in nature

5) Values should be enclosed within square brackets
"""
#
#
#list= [10,10.5,'nafees',True,10]
#
#print(list)             # [10,10.5,'nafees',True,10]
#
#
#
#list=[10,20,30,40]
#
#list[0]            #10
#
#list[-1]           #40
#
#list[1:3]         #[20, 30]
#
#list[0]=100
#
#for i in list:
#         print(i)
#

#
# list is growable in nature. i.e based on our requirement we can increase or decrease the size.
#
#
#
#list=[10,20,30]
#
#list.append("nafees")
#
#list                           # [10, 20, 30, 'nafees']
#
#list.remove(20)
#
#list                            # [10, 30, 'nafees']
#
#list2= list*2
#
#list2                          # [10, 30, 'nafees', 10, 30, 'nafees']
#





# # tuple data types
#
# a= (10000 , 20111 , 40, " nafees", ["list"])
# print(a)
# print(type(a))
# print(id(a))
#
# print(a[0])
# print(a[3])
# print(a[3:4])
# print(a[-2])
#
# # print(t)

# a= (10,)
# print(a)
# print(type(a))

# Tuple is immutable
# indexing or slicing allow

#==================================

# set data type

# s= {10,20,20,30,30,"nafees"}
# print(s)
# print(type(s))
#
# #print(s[1:3])    # TypeError:  indexing are not allow
#
# s.add(1000)
# print(s)
#
# s.remove(20)
# print(s)
#
#
# s2= set()
# print(s2)
# print(type(s2))
#
# s1 = {}
# print(s1)
# print(type(s1))
#====================================
# frozenSet data type

# f = {10,20,20,30,40}
#
# fs= frozenset(f)
# print(fs)
# print(type(fs))
#
# for i in fs:
#     print(i)

#=================================
#dict data type

# d = {101: 10, 202: True, 303: (15,), 203: ["abc"]}
# print(type(d))
#
# print(d[202])
#
# dt = {}
# print(dt)
# print(type(dt))
#
# #d[101]= "verma"
# print(d)
#=================================

# # Range data type
#
# r= range(10)
#
# print(r)            # range(0,10)
# print(type(r))
# print(r[5])

#------------------------------

# a= range(0, 20, 2)
# for x in a:                      # 0, 2, 4, 6 , 8 , 10, 12 , 14, 16 , 18
#         print(x)
#
# print(a[5])                 #  10
#
# a[0]=  7             # TypeError: 'range' object does not support item assignment


# l = list(range(10))
# print(l)
#
# print(l[3: 6])
#
# l[2]= 888
# print(l)


"""
1. sequence of numbers
2. range(10)  ---->     one argument
3. range(10,20)----->   two argument
4. range(10,20,2)----->   three argument

5. order is there  so, indexing slicing  is allow

6. immutable /  we can't  change value
"""
#==========================================

# byte data type

# l = [10,20,30,40]
#
# b = bytes(l)     # b'10,20,30,40'
#
# print(b)                    #  0  to  255
# print(type(b))
#
# print(b[0:2])
# print(b[-1])
#
# for x in b:
#     print(x)

# byte data type is immutable
#==================================

"""byte array data type"""
# x= [10,20,30,40]
# b= bytearray(x)
# print(b)          #  b'10,20,30,40'
# print(type(b))
#
# for i in b:
#     print(i)
#
# print()
#
# b[0]= 231
#
# print(b[0:2])
#
# for i in b:
#     print(i)
#
# # byte array is mutable
# # indexing & slicing allow


# x= [10,255]
# b= bytearray(x)
#
# print(b)

"""in general we can use byte and bytearray  data type  to represent  binary information
like  image, video file etc
"""

#  None data type
"""none  means nothing  or no value associated
"""
# Example:

# def m1():
#     a = 10
#
#
#
# print(m1())
#====================================

# escape character

s = """this is ""  symbol  this ' is '  symbol"""
print(s)
"""

\n     --->   new line 
\t       -->  horizontal tab
\r      ----> carriage return
\b    -->     back space
\f     ->>     form  feed 
\v     -  >    vertical tab
\'      --- >   single  quote
\"     --->    double quote
\\     ---->    back slash symbol

"""



































