from functools import reduce

l= [10,20,30,40,50,60]

res= reduce(lambda x,y: x+y , l)
print(res)
#-----------------------------------


# res= reduce(lambda x,y: x+y, range(1,101))
# print(res)


