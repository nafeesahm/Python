#help("modules")

#=================


import pymysql

con= pymysql.connect(host='107.0.0.1',database='pythondb',user='root',password='220797')

cursor=con.cursor()
cursor.execute("create table employees(eno int(5) primary key,ename varchar(esal double(10,2),eaddr varchar(10))")
print("Table Created...")

sql = "insert into employees(eno, ename, esal, eaddr) VALUES(%s, %s, %s, %s)"
records= [(100,'Sachin',1000,'Mumbai'),
          (200,'Dhoni',2000,'Ranchi'),
          (300,'Kohli',3000,'Delhi')]

cursor.execute(sql,records)

print("Records Inserted Successfully...")
cursor.execute("select * from employees")

data=cursor.fetchall()

for row in data:
    print("Employee Number:",row[0])
    print("Employee Name:",row[1])
    print("Employee Salary:",row[2])
    print("Employee Address:",row[3])
    print()
    print()

con.commit()
con.close()
