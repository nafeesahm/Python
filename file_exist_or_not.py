#how to check a particular file is exist or not
#
# import os
#
# fname = input("enter file name: ")
#
# if os.path.isfile(fname):
#     print("file exist: ", fname)
#
#     f= open(fname,"r")
#
#     file= f.read()
#
#     print("\nThe content of the file is: ")
#     print("*"*40)
#     print(file)
#     print("*"*40)
#
#
# else:
#     print("File not Exist", fname)
#
#     print(":::SORRY YOUR FILE IS NOT THERE:::")
#-----------------------------------------------


# program to find the number of Lines, words, & character in the file
# import os
#
# fname= input("enter file name: ")
#
# if os.path.isfile(fname):
#     print("File Exist :: ", fname)
#
#     f= open(fname, "r")
#     lcount= wcount= ccount= 0
#     for line in f:
#         lcount= lcount+1
#
#         no_of_words_in_current_line= len(line.split())         #return List[]
#         wcount=  wcount + no_of_words_in_current_line          # for words
#
#         no_of_character_in_current_line= len(line)             # length of lines
#         ccount= ccount + no_of_character_in_current_line
#
#
#     print("The Number Of line is: ", lcount)
#     print("the number of words is : ", wcount)
#     print("the no. of character is: ", ccount)
#
# else:
#     print(":::File does't exist:::")


#------------------------------------



# import os , sys
#
# fname = input("enter file name: ")
#
# if os.path.isfile(fname):
#     print("file exist: ", fname)
#
#     f= open(fname,"r")
#
# else:
#     print("File not Exist", fname)
#     sys.exit(0)
#
# print("The content of file is : " )
# data = f.read()
# print(data)

"""Note -- to exit system without executing rest of the program,.."""
"""argument represent status code 0.. means normal termination and it is the default value"""






