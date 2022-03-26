# import pymysql
#
# con = pymysql.connect(host = "localhost", user = "root", password = "220797", database= "employee")
#
# cur = con.cursor()
# print(type(cur))
# print(type(con))

#========================
#
# import pymysql
#
# con = pymysql.connect(host = '127.0.0.1', user= 'root', password= '220797', database= 'employee')
#
# cur = con.cursor()
#
# q = "select * from employee"
# cur.execute(q)
# data = cur.fetchall()           # return in tuple data type
# for row in data:
#     print(row)
#
# con.close()

#-------------------------

#
# import pymysql
#
# con = pymysql.connect(host = '127.0.0.1', user= 'root', password= '220797')
#
# cur = con.cursor()
# cur.execute("use cetpa")              # data base  used
#
# q = "select * from python"           # all employee tables data selected
# cur.execute(q)
#
# data = cur.fetchall()           # return in tuple data type
#
# for roll, name, age , marks in data:                  # itterable item ,,, unpacking
#     print(roll , name, age , marks)
#
# con.close()

#=================

""" insert data in MySQL database"""

# import pymysql
#
# con = pymysql.connect(host = '127.0.0.1', user= 'root', password= '220797')
#
# cur = con.cursor()
#
# cur.execute("use cetpa")              # data base  used
#
#
# cur.execute("insert into python values(53 , 'ahmad', 13, 63)")
#
# con.commit()
# con.close()
#-------------------------------

"""program to save data to csv file from mySQL database using python"""

import pymysql

con = pymysql.connect(host= "127.0.0.1", user= "root", password= "220797")

cur = con.cursor()
cur.execute("use cetpa")

cur.execute("select * from python")
data = cur.fetchall()

f = open(r"C:\Users\NAFEES AHMAD\PycharmProjects\database\file1.csv" , "w")
f.write("Roll , Name , Age , Marks\n")

for roll,name,age,marks in data:
    f.write(f"{roll},{name},{age},{marks}\n")


print("data added successfully")

con.commit()
con.close()







