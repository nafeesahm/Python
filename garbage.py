""" Garbage collector"""
"""
-- garbage collector is assistant which is always runningin the background to distroy useless object, 

-- hence the main objective if garbage colleector  is to distroy the useless object
-- if any obect does not have reference variable then that object eligible for garbage collection..

"""
# how to enable and disable garbage collector in our program
"""by default garbage collector is enabled, """
#
# import gc
# print("garbage collector is enable : ", gc.isenabled())
#
# gc.disable()
# print("garbage collector is enable : ", gc.isenabled())
#
# gc.enable()
# print("garbage collector is enable : ", gc.isenabled())

"""========================================================="""

"""Destructors"""
#    __del__
""" just before destroying an object garbage collector calls destructor to perform clean up activity. 
    (resource deallocation activities like close database connection etc)"""

# once destructor executed then garbage collector autometically destroys that object
# the job of destructor is not destroy object and  it is just perform clean up activities


# import time
# class test:
#
#     def __init__(self):
#
#         print("object initilization....")
#
#
#     def __del__(self):
#         print("fulfill last wish and performing clean up activities...")
#
# t1 = test()
# t1 = None
#
# time.sleep(5)
# print(":::End of application:::")

#================================================

"""Note"""
"""if the object does not contain any reference variable then only it is eligible for garbage collector
i.e..   if the reference count is zero then only object eligible for garbage collector"""
#
# import time
#
# class test:
#     def __init__(self):
#         print("constructor Execution....")
#
#     def __del__(self):
#         print("Destructor Execution...")
#
# t1 = test()
# t2 = t1
# t3 = t2
# del t1                   # delete t1
# time.sleep(5)
# print("object does not destry after deleting t1")
#
# del t2
# time.sleep(5)
# print("object does not destry after deleting t2")
#
# print("I am trying to delete last referencre variable ")
# del t3

# import time
# class Test:
#
#     def __init__(self):
#         print("construction execution...")
#
#     def __del__(self):
#         print("destruction execution...")
#
# list = [Test(), Test() , Test()]
#
# time.sleep(5)
# del list                # all object deleted  , because only one reference variable
#
# print("end of the application...")
#-------------------------
#
# class test:
#
#     def __init__(self):
#         print("constructor execution....")
#
#     def __del__(self):
#         print("destructor execution...")
#
# t1 = test()
# t2 = test()
#                                   # by default , automatically destructor will execute  end of the program
# print("end of the program")

"""as control reaches end of the program , all object which are created as the part of that program are 
by default eligible  for garbage collection"""


#===============================================

# How  to find the number of reference variable of an Object

import sys

class test:
    pass


t1 = test()

t2 = t1

t3 = t2

t4 = t3

print(sys.getrefcount(t1))





































