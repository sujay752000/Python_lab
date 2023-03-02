class Bank:

    def __init__(self):
        self.acnt_no = int(input("Enter your account number : "))
        self.name = input("Enter account holder name : ")
        self.acnt_typ = input("Enter aacount type : ")
        self.balance = 0

    def deposit(self):
        self.balance = self.balance + int(input("Enter your amount to deposit : "))

    def withdraw(self):
        amnt_withdraw = int(input("Enter amount to withdraw : "))
        if amnt_withdraw > self.balance:
            print("Insufficient Balance")
        elif amnt_withdraw <= 0:
            print("Sorry invalid amount")
        else:
            self.balance = self.balance - amnt_withdraw
            print(f"amount withdrwan = {amnt_withdraw}")
            print(f"Current Balance = {self.balance}")

    def display_details(self):

        print(f"Account No = {self.acnt_no}\n"
              f"Account Holder = {self.name}\n"
              f"Account Type = {self.acnt_typ}\n"
              f"Current Balance = {self.balance}\n")


person1 = Bank()

while(True):
    print("\t1.Deposit\n\t2.Withdraw\n\t3.Display\n\t0.Exit")
    opt = int(input("Enter your option : "))

    if opt == 1:
        person1.deposit()
    elif opt == 2:
        person1.withdraw()
    elif opt == 3:
        person1.display_details()
    elif opt == 0:
        print("You are exited")
        break
    else:
        print("Invalid choice !")
