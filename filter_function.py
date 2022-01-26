# # without filter() function
#
# l= [0,1,2,3,4,5,6,7,8,9]
#
# def iseven(x):
#     if x%2==0:               # Condition check
#         return True
#     else:
#         return False
#
# l1= []      #Empty List
#
# for x in l:
#     if iseven(x)==True:       #Function calling
#         l1.append(x)
#
# print(l1)
#----------------------------------

# Filter Function

# l= [0,1,2,3,4,5,6,7,8,9,10]
#
# def iseven(x):
#     if x%2==0:               # Condition check
#         return True
#     else:
#         return False
# for x in l:
#     l1 = filter(iseven , l)
#
# print(l1)
#----------------------------------

# l= [0,1,2,3,4,5,6,7,8,9,10]
#
# l1= list(filter(lambda n: n%2 == 0 ,l))
# print(l1)
#--------------------------------

heroins= ["katrinakaif","anushka","karinaKapoor","salmankhan"]

startwithK= list(filter(lambda name: name[0]=="k", heroins))
print(startwithK)

lenby5= list(filter(lambda name: len(name)%5==0, heroins))
print(lenby5)

odd = list(filter(lambda name: len(name)%2 !=0, heroins))
print(odd)























