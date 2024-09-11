class BankAccount:
    def __init__(self,acc,bal,date,name):
        self.account_number =acc
        self.balance = bal
        self.date_of_opening = date
        self.customer_name = name

    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited Successfully")

    def withDraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Amount WithDrawn Successfully")

        else:
            print("Error")

    def check_Balance(self):
        print(f"Your Current Balance is: {self.balance}")


Acc1 = BankAccount("439A432", 787474, "23/5/2002", "Abbas")
Acc1.deposit(6797)
Acc1.withDraw(4567)
Acc1.check_Balance()
