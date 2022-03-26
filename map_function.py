# Map function  -- without lambda function

l= [2,3,4,5,6]

def squareit(n):
            return n*n

l1= list(map(squareit, l))

print(l1)

#---------------------

#With Lambda Function

# l= [1,2,3,4,5]
#
# l1= list(map(lambda n: n*n , l))
#
# print(l1)
#-----------------------------
#
# l1= [1,2,3,4,5]
# l2= [10,20,30,40,50]
#
# l3= list(map(lambda x,y : x*y ,l1,l2))
# print(l3)

