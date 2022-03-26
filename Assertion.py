# def squareit(x):
#     return x**x
#
# assert squareit(3)==9
# assert squareit(4)==16
# assert squareit(5)==25
#
# print("square of 3 is ", squareit(3))
# print("square of 4 is ", squareit(4))
# print("square of 5 is " , squareit(5))

#=====================
#
# def squareit(x):
#     return x**x
#
# assert squareit(3)==9 , "the square should be 9"
# assert squareit(4)==16, "the square should be 16"
# assert squareit(5)==25, "the square should be 25"
#
#
# print("square of 3 is ", squareit(3))
# print("square of 4 is ", squareit(4))
# print("square of 5 is " , squareit(5))

"""AssertionError: the square should be 9"""

#-----------------------------------------


def squareit(x):
    return x*x

assert squareit(3)==9 , "the square should be 9"
assert squareit(4)==16, "the square should be 16"
assert squareit(5)==25, "the square should be 25"


print("square of 3 is ", squareit(3))
print("square of 4 is ", squareit(4))
print("square of 5 is " , squareit(5))
