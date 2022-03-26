# tell()  -> to know the current curser position(file_pointer)

# f= open("tell_1.txt","r")
# print(f.tell())
# print(f.read(2))
# print(f.read(5))
#
# print(f.tell())
# print(f.read(7))
# print(f.tell())
#--------------------------------------------------
#
# f= open("tell_1.txt","r")
# print(f.tell())
# print(f.seek(3))
# print(f.tell())
#
# print(f.seek(7))
# print(f.read(8))
#
# print(f.seek(20))
# print(f.read())
#
# print(f.seek(0))
# print(f.read())
#----------------------------------
#
f= open("seek.txt","w")

f.write("all student are stupid")

with open("seek.txt", "w+") as f:
    text= f.read()

    print("before modification:")
    print(text)
    print("the current curser position is ", f.tell())

    print("move  the cursor position on 16  index")
    f.seek(16)        # to move the cursor at 17 index
    print("the current cursor position is: ",f.tell())          #  to know the current cursor position

    data= f.write("GEMS!!!!")
    f.seek(0)

    text=f.read()

    print("after modification: ")
    print(text)


