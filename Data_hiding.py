"""Data hiding"""
# outside person should not access our data directly ,our internal data will not go out directly,
# this oops feature is nothing but data hiding

# by using private variable we can implement data hiding
"""The main advantage of data hiding is security """


class Account:
    def __init__(self , balance):
        self.__balance = balance               # private variable

    def getbalance(self):
                             ♦    # validation / Authentication
        return self.__balance

b = Account(10000)
#print(b.balance)               # outside person should not access , our data directly...

print(b.getbalance())





