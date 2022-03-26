# fname= input("Enter file Name: ")
#
# f= open(fname, 'w')
#
# while True:
#         data= input("ENTER SOME DATA:: ")
#         f.write(data + '\n')
#
#         option= input("DO YOU WANT TO ADD SOME MORE DATA: [YES/ NO]:: ")
#         if option.lower()== "no":
#              break
# print(":::YOUR PROVIDED DATA WRITTEN TO THE FILE SUCCESSFULLY::: ")
# f.close()
#
# ---------------------------------------------------------------

# f= open("file_handling1.txt","r")
#
# line1= f.readline()
# print("first mobile number is: ", line1,end="")
#
# line2= f.readline()
# print("second mobile number is: ", line2, end= "")
#
# line3= f.readline()
# print("third mobile number is: ", line3, end="")
#
# line4= f.readline()
# print("fourth mobile number is: ", line4, end="")
#
# f.close()
#------------------------------------------------------

# f= open("file_handling1.txt","r")
#
# line= f.readline()
#
# while line != "":
#                 print(line, end= "")
#                 line= f.readline()
#
# f.close()
#-----------------------------------------
#
# f= open("readlines.txt", "r")
#
# l= f.readlines()
# print(l)
# for lines in l:
#             print(lines, end="")
#
# f.close()
#---------------------------------------------

# copy the data from one file to another file

# olddata= open("datacopy.txt", "r")
# newdata= open("newdata.txt", 'w')
#
# data= olddata.read()
# data1= newdata.write(data)
#
# print(data)
# print(data1)
#
# print("the data copied successfully!!!")
#
# olddata.close()
# newdata.close()
#---------------------------------

# file closed without using close() method
with open("data1.txt","w") as f:
                f.write("nafees_ahmad\n")
                f.write("matin_ahmad\n")
                f.write("anis_ahmad\n")
                f.write("sheesh_ahmad")
                print("Is file closed: ",f.closed)

print("Is file closed: ",f.closed)















