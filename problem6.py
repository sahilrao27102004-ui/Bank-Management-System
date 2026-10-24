#bank account system 

class BankAccount:

    def __init__(self,holder,acc_no,balance):
        self.holder=holder
        self.acc_no=acc_no
        self.balance=balance
        self.transactions=[]

    def debited(self):
        debit=int(input("Enter the debit amount: "))
        if debit<=0:
            print("Entered wrong Value")
        elif debit>self.balance:
            print("Insufficient Balance!")
        else:
            self.balance-=debit
            print(f"Rs {debit} is debited from your account.")
            print(f"Available ammount is: {self.balance}")
            self.transactions.append(f"Rs {debit} debited.")


    def credited(self):  
        credit=int(input("Enter the credit amount: "))
        if credit<=0:
            print("Entered wrong value")
        else:
            self.balance+=credit
            print(f"Rs {credit} is credited to your account.")
            print(f"Available amount is: {self.balance}")
            self.transactions.append(f"Rs {credit} credited.")


class saving_Account(BankAccount):
    def __init__(self,holder,acc_no,balance,interest_rate):
        super().__init__(holder,acc_no,balance)
        self.interest_rate=interest_rate
        self.interest_calculated=False

    def calculated(self):
        if self.interest_calculated:
            print("Interest has already calculated")
            return
        
        interest=self.balance*self.interest_rate/100
        self.balance+=interest
        self.interest_calculated=True   

        print("Interest rate:",self.interest_rate)
        print("Interest added: Rs", interest)
        print("Available balance with interest: ", self.balance)

        self.transactions.append(f"Rs {interest} credited.")

    def check_balance(self):
        print(f"Your balance is {self.balance} ")
    
    def display_history(self):
        if not self.transactions:
            print("There is no any transaction")
        else:
            for transaction in self.transactions:
                print(transaction)
accounts={
    10193:saving_Account("Sahil",10193,5000,5),
    45682:saving_Account("Ankit",45682,5000,5),
    90110:saving_Account("Chintu",90110,5000,5)
}

def create_account():
    holder=input("Enter your name: ")
    acc_no=int(input("Enter the account number: "))
    balance=int(input("Enter account opening amount: "))
    intrest_rate=5
    
    if acc_no in accounts:
        print("Account already exists")
        return None
    elif balance<0:
        print("Enter a valid amount")
        return None
    else:
        accounts[acc_no]=saving_Account(holder,acc_no,balance,intrest_rate)
        print("Account created succesfully...")
        print("Fixed interest rate: 5%")
        return acc_no


while True:
    try:
        acc_no=int(input("Enter your account number:"))
        if acc_no in accounts:
            current_account=accounts[acc_no]
            print(f"Welcome {current_account.holder} ")
            break
        else:
            print("Account not found! Please try after creating a new account...")

    except ValueError:
        print("Please enter the valid account number!")

while True:
    print("\n*****BANK*****")
    print(f"Account Holder:{current_account.holder}")
    print(f"Account Number:{current_account.acc_no}")


    print("\n1. Debit Amount")
    print("2. Credit Amount")
    print("3. Check Balance")
    print("4. Calculate Interest")
    print("5. Transaction History")
    print("6. Create Account")
    print("7. Change account")
    print("8. Exit")

    try:
        choice=int(input("Enter the choice: "))

        if choice==1:
            current_account.debited()
        elif choice==2:
            current_account.credited()
        elif choice==3:
            current_account.check_balance()
        elif choice==4:
            current_account.calculated()
        elif choice==5:
            current_account.display_history()
        elif choice==6:
            new_acc_no=create_account()
        
            if new_acc_no is not None:
                current_account=accounts[new_acc_no]
                print("Account selected successfully")
                continue
        elif choice==7:
            new_acc_no=int(input("Enter the account number to switch: "))
            if new_acc_no in accounts:
                current_account=accounts[new_acc_no]
                print(f"Account switched to {current_account.holder}")

            else:
                print("Not found! Account unchanged") 

        elif choice==8:
            print("Thankyou for using our bank...")
            break

        else:
            print("choice doesn't exist")
            continue

    except ValueError:
        print("please enter a valid input!")
    


