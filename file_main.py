# f= open("nafeesdata06.txt",'r')
#
# print("file_name: ",f.name)
# print("file_mode: ",f.mode)
# print(f.read())
#
# print("is file closed: ", f.closed)                  # False
# print("is file writable: ", f.writable())            # False
# print("is file readable: ", f.readable())            # True
#
# f.close()                     # we close the file
# print("file_closed")
# print("is file closed: ", f.closed)          # True
#------------------------

# f= open("file_handling1.txt","w")
# f.write("nafees\n")
# f.write("ahmad\n")
# f.write("is a good boy:\n")
# f.write("bahubali2 is good movie in all over the world\n")
# f.write("Hey all.. i am bot how are you")
# f.close()
#
# print("data is saved successfully,,,,,")

#--------------------------------
f= open("listdata1.txt","w")
l= ['nafees\n','ahmad\n','anis\n','faiz\n']
#d= {"nafees":100,"ahmad":50}
#d= {100: 'nafees', 200:'ahm'}       # when we access values from the dictionary/  key should be str type only
f.writelines(l)
""" to saved the txt data in form of collection related
                                       data type like list, dict, tuple, set"""

print("list of files saved successfully,,,,")
f.close()
















