import sys

class customer:
    """mini bank application developed by nafees"""

    bankname= "nafeesbank"
    def __init__(self, name, balance=0.0):

        self.name= name
        self.balance= balance

    def deposite(self, balance):
        self.balance= self.balance + balance
        print("Balance deposited sucessfully", self.balance)

    def withdraw(self, balance):
        if balance>self.balance:
            print("Insufficiant Funds...")
            sys.exit()
        else:
            self.balance= self.balance - balance
            print("withdraw sucessfully", self.balance)

    def amount(self):
        print("your available balance is: ", self.balance)

print("welcome to ", customer.bankname)

name = input("Enter your A/C no- : ")
c = customer(name)

while True:
    print("#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/")
    n = input("\nEnter your choice\ndeposite= d \nwithdraw= w\ncheck balance= b\nexit= e\n ::::::: please select ->      ")
    if n.lower() == "d":
        balance= float(input("Enter amount: "))
        c.deposite(balance)                               # for deposite

    elif n.lower() == "w":
        bal = float(input("Enter amount: "))
        c.withdraw(bal)                                # for withdraw

    elif n.lower() == "b":
        c.amount()                                       # for balance check

    elif n.lower() == "e":
        print("Thanks for using nafeesbank")
        sys.exit()                                            # for exit

    else:
        print(":::invalid choice:::")
    print("#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#//#/#/#/")




