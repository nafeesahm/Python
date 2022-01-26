# def even_odd(number):
#     if number%2==0:
#         print("number is even")
#     else:
#         print("number is odd")
#
# even_odd(10)
# even_odd(15)
#-------------------------

#WRITE A FUNCTION TO FIND FACTORIAL OF GIVEN NUMBER
def factorial(num):
                result= 1
                while num>=1:
                    result=result*num
                    num= num-1
                return result

print(" the factorial is: ",factorial(3))

for i in range(1,6):
    print("the factorial of",i,"is ",factorial(i))

