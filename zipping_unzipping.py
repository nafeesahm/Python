# Zipping and Unzipping Files:
# To create zip file

# from zipfile import *
# f= ZipFile("zipfiles.zip", "w", ZIP_DEFLATED)
#
# f.write("zipfile1.txt")
# f.write("zipfile2.txt")
# f.write("zipfile3.txt")
#
# f.close()
# print("THE ZIP FILE CREATED SUCCESSFULLY")

#---------------------------
"""
from zipfile import *
f= ZipFile("zipfiles.zip", "w", ZIP_DEFLATED)

while True:
            filename= input("Enter File_Name: ")

            f.write(filename)

            n= input(" Do you want to add more file: YES / NO -  " )

            if n=='no' or n=='NO':
                break

f.close()
print("THE ZIP FILE CREATED SUCCESSFULLY")
"""
#----------------------------------------
# To perform unzip Operation:

from zipfile import *
f=ZipFile("zipfiles.zip",'r',ZIP_STORED)
names=f.namelist()
for name in names:
        print( "File Name: ",name)
        print("The Content of this file is:")
        f1=open(name,'r')
        print(f1.read())
        print()

















