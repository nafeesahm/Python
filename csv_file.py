#  Writing Data to CSV File:
# import csv
#
# with open("csv_file.csv", "w", newline='') as f:          # newline is used for removing blank line in csv file
#
#     w= csv.writer(f)         #  return csv writer object
#     w.writerow(["FULL_NAME","MOBILE_NO.","ADDRESS","SALLARY"])
#
#     n= int(input("Enter How Many Data you want to enter: "))
#
#     for i in range(n):
#         fname= input("Enter full name: ")
#         mobile= int(input("Enter mobile number: "))
#         address= input("Enter Employee Address: ")
#         sallary= int(input("Enter Employee sarray: "))
#
#         w.writerow([fname, mobile, address, sallary])
#
# print("Employee data written to csv successfully")


#-----------------------------------------------------------

# Reading Data from CSV File:

f= open("csv_file.csv",'r')
r= csv.reader(f)      #returns csv reader object
data= list(r)
# print(data)
for line in data:
    for word in line:
            print(word,"\t",end='')
    print()












