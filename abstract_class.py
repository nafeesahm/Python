#Abstract Method

"""sometime we don't know about implementation, still we can declare a method . such type of method
are called abstract method """
"""abstract method has only declaration but not implementation"""
"""in python we can declare abstract method by using @abstractmethod  decorator as follows: 

@abstractmethod
def m1(self):
    pass
"""

"""@abstractmethod method decorator present in abc module.. Hence,compulsory we should import abc module , 
otherwise we will get Error"""
""" ○   abc -> abstract base class module"""

# class test:
#     @abstractmethod
#     def m1(self):
#         pass
# t = test()
# t.m1()                  # NameError: name 'abstractmethod' is not defined

#○○○○○○○
#
# from abc import *
# class test:
#     @abstractmethod
#     def m1(self):
#         pass
#
# t = test()
# t.m1()
#------------

#
# from abc import *
#
# class fruit:
#     @abstractmethod
#     def teste(self):
#         pass


#••••••••••••••••


# Abstract Class

"""sometime implementation of class is not complete ,   
such type of partially implemented classes are called abstract class"""

"""Abstract class -> partially implemented class"""    # thora thora krke

"""Every abstract class in python should be child class of ABC class , which is present in abc module"""
"""ABC -> Abstract base class"""

"""child classes are responsible to provide implementation  for parent class abstract method """

#
# from abc import *
# class Test:
#     pass                       # it does not contain any abstract method ,,, it is concrete class
#
# t = Test()


#===========

# from abc import *
# class Test(ABC):
#     pass                        #  it does not contain any abstract method
#
# t = Test()
#---------------

#
# from abc import *
# class Test(ABC):
#     @abstractmethod
#     def m1(self):
#         pass
#                             # TypeError: Can't instantiate abstract class Test with abstract method m1
# t = Test()
#------------------

#
# from abc import *
# class Test(ABC):
#     @abstractmethod
#     def m1(self):
#         pass
#                             # TypeError: Can't instantiate abstract class Test with abstract method m1
# t = Test()

#================

#  abstract class with abstract method instantiation is not possible
# parent class abstrat method should be implemented in the child class .  otherwise we cannot intantiate child class.
# if we are not creating child class object then we won't get any error

"""case - 1 """
# from abc import *
# class vehicle(ABC):
#     @abstractmethod
#     def getnoofwhere(self):
#         pass
#
# class Bus(vehicle):
#     pass
"""it is valid because we are not creating any object"""

"""case - 2"""
# from abc import *
# class vehicle(ABC):
#     @abstractmethod
#     def noofwheel(self):
#         pass
#
# class bus(vehicle):
#     pass                         # we are not passing any implementation to the parent class
#
# b = bus()
# b.noofwheel()         """ TypeError: Can't instantiate abstract class bus with abstract method noofwheel"""


""" if we are extending abstract class and does not override its abstract method then child class is also abstract 
 and implementation is not possible """


from abc import *
class vehicle(ABC):
    @abstractmethod
    def noofwheel(self):
        pass

class bus(vehicle):
    def noofwheel(self):
        return 7

class auto(vehicle):
    def noofwheel(self):
        return 3

b = bus()
print(" no of wheel in bus : ",b.noofwheel())

a = auto()
print(" no of wheel in auto : ",a.noofwheel())

# abstract class can contain both abstract and non-abstract method  also
















