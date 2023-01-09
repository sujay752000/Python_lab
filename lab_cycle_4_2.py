class BankAccount:

    def __init__(self):
        self.accounnt_no = int(input("Enter the acount number : "))
        self.name = input("Enter the account holder name : ")
        self.typ_of_ac = input("Enter the type of account : ")
        self.balance = int(input("Enter the balance :"))

    def deposit(self):
        self.balance = self.balance + int(input("Enter the amount you want to deposit : "))

    def withdraw(self):
        self.balance = self.balance - int(input("Enter the amount you need to withdraw"))

    def display(self):
        print(f" Account no : is {self.accounnt_no} \n Name is : {self.name} \n Type of account is {self.typ_of_ac} \n Balance is {self.balance}")

person1 = BankAccount()
while(True):
    option = int(input("\npress \n    1. To Check Account details\n    2. To Deposit\n    3. To Withdraw\n    4. exit"))
    if option == 1:
        person1.display()
    elif option == 2:
        person1.deposit()
    elif option == 3:
        person1.withdraw()
    elif option == 4:
        print("You are exited :")
        break
    else:
        print("Invalid choice : \n")

