"""SET Data Structure"""


# s =set()
# print(type(s))
# print(s)
# s.add(10)
# s.add(20)
# s.add(30)
# s.add(10)
# print(s)




# l = [10,20,30,40,50,6]
# print(l)
# s = set(l)
# print(s)

# print(s[0])        #TypeError: 'set' object is not subscriptable


# print(set(range(10)))



"""important Function of set"""

"""
1 . add(x)
2 . update(x, x, x)    multiple arguments we cn take
3 . copy(x)
4 . pop()
5 . remove(x)
6 . discard(x)
7 . clear(x)
"""
#
# s = {10 ,20, 30}
# s.add(40)
# print(s)
# s.add(333)
# print(s)

# s = {10,20,30}
# l = [40,50,60,10]
# s.update( l , range(4))
# print(s)
#
# s = {1,2,34,5,6,7 ,9}
# l = [11,22,33, 77]
# e = [9.9, 7 , 76]
# s.update(l,e , "100" , "nafees" , "66" , "nafees")
# print(s)


"""What is the difference between add() and update() Functions in Set?
 We can use add() to add individual item to the Set,where as we can use update() 
function to add multiple items to Set.
 add() function can take only one argument where as update() function can take any 
number of arguments but all arguments should be iterable objects.
"""


"""Which of the following are valid for set s?
1) s.add(10)
2) s.add(10,20,30)  TypeError: add() takes exactly one argument (3 given)
3) s.update(10)  TypeError: 'int' object is not iterable
4) s.update(range(1,10,2),range(0,10,2))
"""
#
# s= {10 , 20 , 30}
# print(s)
#
# s1 = s.copy()
# print(s1)

#
# s = {40 , 99, 30 , 88, 40 , 44 , 99}
# print(s)
#
# w = s.pop()
# for x in s:
#         if x==w:
#             print("value pop")
#         else:
#             print(x)


#
# s = {40,30,20, 99}
# s.remove(40)
#
# print(s)
#



# s = {10,20,304,40}
#
# s.discard(20)
# print(s)
#
# s.clear()
# print(s)

# i = 0
# set  =set()
# while i<=5:
#         n = eval(input("enter any values : "))
#
#         set.add(n)
#         i+=1
#
# print("All values added succerssfully: ", set)
#
# set.clear()


# mathematical opperation on set

"""
1 . union()
2 . intersection()
3 . defference()
4 . symmetric difference()

"""
#
# x = {10,20,30,40,50}
# y = {30,40,50,60}
# print(x.union(y))
# print(x|y)
#
#
#
# x = {10,20,30,40,50}
# y = {10,30,40,50,60}
# z = {10,20,3,4}
# print(x.intersection(y,z))
# print(x&y)
# print(x&y&z)

"""difference()"""   # x -y
# y = {10,30,40,50,60}
# x = {10,20,30,40,50}
#
# print(y.difference(x))
# print(x- y)


#
# x = {10,20,30,40}
# y = {30,40,50,60}
# print(x.symmetric_difference(y))    # 10 50 20 60
# print(x ^ y)
#
#
# print(x.symmetric_difference_update("10"))


#
# x = {10,20,30,40}
# y = {30,40,50,60}
#
# update = x.symmetric_difference_update(y)
# print("x : " , x)
# print("y : " , y)
#
# print("Result : " , update)
""" x :  {10, 50, 20, 60}
    y :  {40, 50, 60, 30}
    Result :  None
"""
#========================================================================
"""set comprehension"""
s= {x*x for x in range(1,6)}
print(s)
print(type(s))
print()

s= {2**x for x in range(1,6)}
print(s)
print(type(s))
#=========================================
"""removing duplicate items from the list"""
"""1st approach"""
l= [10,10,20,30,20,10,40]
print(l)
s= set(l)
print(s)
print(type(s))

l1 = list(s)
print("after remove duplicate: ", l1)
print(type(l1))


""""2nd  approach"""
l= [10,10,20,30,10,20,30]
l1 = []
for x in l:
    if x not in l1:
        l1.append(x)
print(l1)

#*******************************
"""write a program to print different vowel present in the given word"""
# word= input("enter any word to search for vowel : ")
# s = set(word)                                                 # duplicate removed
# print(s)
# v= {'a' , 'e', 'i', 'o', 'u'}
# print(v)
#
# result = s.intersection(v)
# print("The different vowels present in {} are : {}".format(word, result))








