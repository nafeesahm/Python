#REGULAR EXPRESSION

import re
s= """ ndls nafees@gmail.com ,kakaLo madhurchauhan@yahoo.com m; hvfshiowh
        bvdb-sv0-jb jai@cetpa.com gyiegwIUO2 abc@gmail.com"""

p= r"\w+@\w+[.]\w+"
res= re.findall(p, s)
print(res)
#----------------------------------------
# import re
# s= "welcome to cetpa infotech pvt ltd"
#
# p= r'[abcd]'         #or  (r'[a-d]')    it will find out any character either a,b,c, or d
# res= re.findall(p, s)
# print(res)
#----------------------------------------

# import re
# s= " welcome 1234  @#456 to \+CET \cetpa 634"
# p= r'[^a-z]'
# res= re.findall(p,s)
# print(res)
#------------------------------------------

# import re
# s= "welcom to cetpa infotech pvt ltd , cetpa is a training company "
#
# p= r'cetpa'
# res= re.findall(p, s)
# print(res)     # output= ['cetpa', 'cetpa']
#----------------------------------------

# import re
# s= "welcome 1234 @#456 to \tCET \ndls 786"
# p= r'[a-zA-Z0-9]{4}'    # it will search 4 character from each word which is alphanumeric
# res= re.findall(p,s)
# print(res)    # output= ['welc', '1234']
#---------------------------------------------

# import re
# s= "welcome 1234 @#456 to \tCET \ndls 786"
# p= r'\w{2,7}'   # 7 have first priority
# res= re.findall(p,s)
# print(res)
#-------------------------------------------------

# import re
# s= """ndls nafees@gmail.com ,kakaLo madhurchauhan@yahoo.com m; hvfshiowh
#          bvdb-sv0-jb jai@cetpa.com gyiegwIUO2 abc@gmail.com"""
#
# p= r'\w{1,}@\w{1,}\.\w{1,}'
# res=re.findall(p,s)
# print(res)
#---------------------------------------

# import re
# s= """ndls nafees@gmail.com ,kakaLo madhurchauhan@yahoo.com m; hvfshiowh
#          bvdb-sv0-jb jai@cetpa.co.in gyiegwIUO2 abc@gmail.com mbvchjgsdy ahmad.nafees019@gmail.com"""
# p= r'\w+[.]?\w*@\w+[.]\w+[.]?\w+'
# res=re.findall(p,s)
# print(res)
#-----------------------------
"""
import re
s='anurag kapil saif_ali madhur nafees'
p= r'^anurag'    #start with anurag

#p= r'nafees$'   #ends with nafees

res=re.findall(p,s)
print(res)  
"""