# f1= open('DSC_0212-02.jpg','rb')
#
# data1= f1.read()
# print(data1)
# print(type(data1))
#
# f2= open("copy_image.jpg","wb")
# f2.write(data1)
# print("copy_image.jpg  file is ready")
#
# f1.close()
# f2.close()
# ---------------------------


# copy one binary file to another file

f1= open('DSC_0212-02.jpg','rb')
imagebytes=f1.read()
#print(type(imagebytes))

f2= open('copied_file.jpg','wb')
f2.write(imagebytes)
print('New Image is available with the name: ' , f2.name)

f1.close()
f2.close()


