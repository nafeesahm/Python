"Customer Management System"

print("::::::::::::::::::::::::::::::::")
print(":::CUSTOMER MANAGEMENT SYSTEM:::")
print("::::::::::::::::::::::::::::::::")

cusid= []
cusname= []
cusage= []
cusmob= []


def addcustomer(id, name, age, mob):
    cusid.append(id)
    cusname.append(name)
    cusage.append(age)
    cusmob.append(mob)

def searchcustomer(id):
    index_no= cusid.index(id)
    name= cusname[index_no]
    age= cusage[index_no]
    mob= cusmob[index_no]

    return name, age, mob

def updatecustomer(id, name, age, mobile):
    index_no= cusid.index(id)
    cusname[index_no]= name
    cusage[index_no]= age
    cusmob[index_no]= mobile

def deletecustomer(id):
    index_no= cusid.index(id)     # using index method to find index number
    cusname.pop(index_no)
    cusage.pop(index_no)
    cusmob.pop(index_no)



while True:
    choice= input("""  
                  press- 1 to add new customer
                  press- 2 to search customer
                  press- 3 to update customer
                  press- 4 to delete customer
                  press- 5 to view all customers
                  press- 6  to exit
                  Enter Your Choice: """)

    if choice== '1':
        newid= int(input("Enter customer id: "))
        newname= input("Enter customer Name: ")
        newage= int(input("Enter Customer age: "))
        newmob= int(input("Enter customer mobile number: "))

        addcustomer(newid, newname, newage, newmob)
        print()
        print("Customer Added successfully....!!!")
        print()

    elif choice== '2':
        searchid= int(input("Enter Customer Id to Search  Detail: "))

        searchname, searchage, searchmob = searchcustomer(searchid)
        print("The Required customer details are: ")
        print(f'ID: {searchid}, NAME: {searchname}, AGE: {searchage}, MOB: {searchmob}')

    elif choice== '3':
        updateid= int(input("Enter Customer Id to Update Details: "))
        updatename= input("Enter Updated name: ")
        updateage = int(input("Enter Updated age: "))
        updatemob= int(input("Enter Updated Mobile number: "))

        updatecustomer(updateid, updatename, updateage, updatemob)
        print()
        print("Customer Updated Successfully..!")
        print()

    elif choice== '4':
        deleteid = int(input("Enter Customer ID to Delete Details: "))
        deletecustomer(deleteid)
        print()
        print("Customer Deleted Successfully...!")
        print()

    elif choice== '5':
        print("The Customer Details are : ")
        print(f"ID \t\t\t NAME \t\t\t AGE \t\t\t MOBILE \n")

        for i in range(len(cusid)):
                print(f"{cusid[i]} \t\t {cusname[i]} \t\t {cusage[i]} \t\t {cusmob[i]}\n")

    elif choice== '6':
        print(":::Thanks For Using Our CMS:::")
        break

    else:
        print("Incorrect choice...")

















